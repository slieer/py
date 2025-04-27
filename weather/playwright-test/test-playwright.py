import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://www.oschina.com/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("OSCHINA - 中文开源技术交流社区"))

def test_get_started_link(page: Page):
    page.goto("https://www.oschina.com/")

    # get_by_role 是一个方法，用于根据 ARIA 角色定位元素。
    # Click link: <a href="https://www.oschina.net/news" class="tabs-link news">资讯</a> 
    page.get_by_role("link", name="资讯").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="OSCHINA - 中文开源技术交流社区")).to_be_visible()