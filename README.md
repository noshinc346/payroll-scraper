# Payroll Portal Scraper

This project demonstrates web scraping automation using Selenium in Python to log into a mock payroll portal, extract pay history data, and save it into a JSON and CSV file.

## Features:
- Automated login using Selenium
- Data extraction from a payroll portal
- Data export in JSON and CSV formats

## How to Run:
1. Clone the repository:
   ```bash
   git clone https://github.com/noshinc346/payroll-scraper.git
2. Navigate to project folder:  
    cd payroll-scraper
3. Set up the virtual environment and install         dependencies:
    python -m venv venv
    source venv/bin/activate  # For Mac/Linux
    pip install -r requirements.txt
4. Run the scraper:
    python scraper.py
5. Check the output folder for paychecks.json and paychecks.csv

## Tools Used:
Python
Selenium
JSON, CSV
ChromeDriver (make sure to have the correct version installed)
