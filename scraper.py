from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os

# Set up the Chrome driver
driver_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"  # Optional, only needed if you run into driver issues

# Use Selenium's built-in driver manager (you can customize this if needed)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background
driver = webdriver.Chrome(options=options)

# Open the mock HTML file locally
file_path = f"file://{os.getcwd()}/pay_history.html"
driver.get(file_path)

time.sleep(1)  # Give it a moment to load

# Scrape table rows
rows = driver.find_elements(By.XPATH, "//table[@id='pay-history']/tr")[1:]  # skip header
data = []

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    date = cols[0].text
    employer = cols[1].text
    amount = cols[2].text
    data.append({"date": date, "employer": employer, "amount": amount})

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("output/pay_history.csv", index=False)
print("✅ Data scraped and saved to output/pay_history.csv")

driver.quit()
