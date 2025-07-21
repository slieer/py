from playwright.sync_api import sync_playwright
from datetime import datetime
from dateutil.relativedelta import relativedelta
import config as cfg
import os
import time

# Calculate last month's receipt directory
current_date = datetime.now()
last_month_date = current_date - relativedelta(months=1)
last_month_name = last_month_date.strftime("%B")
year = last_month_date.year
base_receipt_path = f"{cfg.RECEIPT_DIR_ROOT}_{last_month_name}_{year}/receipts"
os.makedirs(base_receipt_path, exist_ok=True)

with sync_playwright() as p:
    # Persistent context for maintaining sessions
    user_data_dir = "/tmp/playwright-profile"

    context = p.chromium.launch_persistent_context(
        user_data_dir=user_data_dir,
        headless=False,
        args=[
            "--disable-webauthn",
            "--use-fake-device-for-media-stream",  # Simulate fake USB device for WebAuthn
            "--use-fake-ui-for-media-stream",  # Fake all WebAuthn UI prompts
            "--disable-features=WebAuthentication,WebAuthnTouchId",
            "--disable-password-manager-reauthentication",
        ]
    )

    page = context.new_page()

    # Log in to Amazon
    page.goto("https://www.amazon.com/your-orders/orders?timeFilter=last30")


    # Check if the email field exists before interacting with it
    email_locator = page.locator("#ap_email")
    
    if email_locator.count() > 0:
        page.fill("#ap_email", f"{cfg.USERNAME}")
        page.click("#continue")
        #page.fill("#ap_email", f"{cfg.USERNAME}")
        #page.click("#continue")
    pass_locator = page.locator("#ap_password")
    if pass_locator.count() > 0:
        time.sleep(3)
        page.fill("#ap_password", f"{cfg.PASSWORD}")
        page.click("#signInSubmit")

    receipt_num = 1
    page_num = 1
    has_next_page = True

    while has_next_page:
        print(f"Processing page {page_num}")
        page.wait_for_selector("a:has-text('View invoice')", timeout=60000)
        invoices = page.locator("a:has-text('View invoice')")
        invoice_urls = invoices.evaluate_all("elements => elements.map(el => el.href)")

        for url in invoice_urls:
            if not url.startswith("http"):
                url = f"https://www.amazon.com{url}"

            print(f"Navigating to: {url}")
            page.goto(url)
            page.wait_for_load_state("load")
            receipt_path = f"{base_receipt_path}/amazon_{receipt_num}.pdf"
            page.pdf(path=receipt_path)
            receipt_num += 1
            page.go_back()
            page.wait_for_load_state("load")

        next_button = page.locator("a:has-text('Next')")
        if next_button.is_visible():
            next_button.click()
            page.wait_for_load_state("load")
            page_num += 1
        else:
            has_next_page = False

    print("All pages processed!")
    context.close()
