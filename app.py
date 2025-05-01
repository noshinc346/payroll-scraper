from flask import Flask, jsonify
import json

app = Flask(__name__)

# Assuming you have a JSON file where you store the paychecks data
@app.route("/paychecks", methods=["GET"])
def get_paychecks():
    try:
        with open("output/paychecks.json", "r") as file:
            paychecks_data = json.load(file)
        return jsonify(paychecks_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# New endpoint for /payroll
@app.route("/payroll", methods=["GET"])
def get_payroll():
    try:
        with open("output/paychecks.json", "r") as file:
            paychecks_data = json.load(file)
        
        total_payroll = sum(paycheck["amount"] for paycheck in paychecks_data)
        
        payroll_info = {
            "total_payroll": total_payroll,
            "num_employees": len(paychecks_data),
            "average_paycheck": total_payroll / len(paychecks_data) if paychecks_data else 0
        }
        
        return jsonify(payroll_info), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
