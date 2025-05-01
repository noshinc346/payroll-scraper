# 🧾 Payroll Scraper & API Project

This project simulates an integration with a payroll system that lacks an API. It uses **Selenium** to scrape pay history data from a local HTML file and serves that data via a **Flask API**. It mimics the kind of detective work required to integrate undocumented systems, like those you'd encounter at companies such as **Pinwheel**.

---

## 🚀 Features

- ✅ Scrapes pay history data (date, employer, amount) from a local HTML file using Selenium.
- ✅ Cleans and stores data in both `.json` and `.csv` formats.
- ✅ Exposes the data through a RESTful Flask API:
  - `/paychecks` – returns raw paycheck data.
  - `/payroll` – returns aggregated payroll statistics.
- ✅ Modular file structure for easier extensibility.

---

## 🗂 Project Structure
payroll-scraper/ │ ├── app.py # Flask API serving the scraped data ├── scraper.py # Selenium script for scraping pay history ├── pay_history.html # Local HTML file acting as the payroll dashboard ├── styles.css # Styling for the HTML page ├── output/ │ ├── paychecks.json # JSON output of scraped data │ └── paychecks.csv # CSV output of scraped data ├── requirements.txt # Python dependencies └── README.md # Project documentation

## 💻 How to Run

### 1. Set Up Environment
```bash
git clone https://github.com/your-username/payroll-scraper.git
cd payroll-scraper
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```
### 2. Run Scraper
```bash 
python scraper.py
```
### 3. Run Flask API
```bash 
python app.py
```
Visit:
http://127.0.0.1:5000/paychecks – View scraped paycheck data
http://127.0.0.1:5000/payroll – View total payroll, employee count, and average paycheck

## 🗂 Sample Data Source 
HTML Source (pay_history.html):
<table id="pay-history">
  <tr>
    <th>Date</th>
    <th>Employer</th>
    <th>Amount</th>
  </tr>
  <tr>
    <td>2024-03-15</td>
    <td>TechWave Solutions</td>
    <td>$2,800.00</td>
  </tr>
</table>


## 📌 Why This Project?
It demonstrates:

🔍 Web scraping and automation with Selenium

🧠 Data cleaning and transformation

🌐 Building and exposing RESTful APIs with Flask

💾 Working with structured data (CSV/JSON)
