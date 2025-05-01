from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Payroll Scraper App!"

@app.route('/paychecks')
def paychecks():
    try:
        # Load data from the JSON file
        with open('output/paychecks.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
