from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import csv
import os

# Global variable to store payroll data
payroll_data = []

def scrape_payroll():
    global payroll_data

    # Set up Selenium WebDriver (using Chrome in this example)
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode

    driver = webdriver.Chrome(options=options)

    # Replace with the local HTML file path
    html_file_path = os.path.abspath("pay_history.html")  # Make sure this points to your actual HTML file

    try:
        # Step 1: Open the local HTML file
        driver.get("file://" + html_file_path)  # Loads the local HTML file
        time.sleep(2)  # Wait for the page to load

        # Step 2: Extract paycheck data
        data = []
        
        # Find the table by its ID
        table = driver.find_element(By.ID, "pay-history")
        
        # Loop through all rows of the table, starting from the second row (skipping header row)
        rows = table.find_elements(By.TAG_NAME, "tr")[1:]
        
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 3:
                data.append({
                    "date": cols[0].text.strip(),
                    "employer": cols[1].text.strip(),
                    "amount": float(cols[2].text.strip().replace("$", "").replace(",", ""))
                })

        # Save the scraped data to the global variable
        payroll_data = data

        # Step 3: Export to JSON (optional)
        with open("output/paychecks.json", "w") as f:
            json.dump(data, f, indent=2)

        # Step 4: Export to CSV (optional)
        with open("output/paychecks.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["date", "employer", "amount"])
            writer.writeheader()
            writer.writerows(data)

        print("✅ Data scraped and saved to output/paychecks.json and .csv")

    except Exception as e:
        print("❌ Error:", e)

    finally:
        driver.quit()

# Call the scrape function directly when the script is run
if __name__ == "__main__":
    scrape_payroll()

