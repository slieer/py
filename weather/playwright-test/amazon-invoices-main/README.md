# amazon-invoices
A python tool that utilizes playwright to download receipts and save them as pdfs. 

# Create Virtual Environment
python -m virtualenv venv

# Activate Virtual Environment
. venv/bin/activate

# Install requirements 
pip install -r requirements.txt

# Get Playwright browsers
playwright install

# Edit config.py template
SET USERNAME, PASSWORD, and RECEIPT_DIR_ROOT

# Execute get_receipts
python get_receipts.py