from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Route to get paychecks data
@app.route("/paychecks", methods=["GET"])
def get_paychecks():
    try:
        # Check if the file exists before attempting to open it
        if not os.path.exists("output/paychecks.json"):
            return jsonify({"error": "Payroll data file not found"}), 404
        
        with open("output/paychecks.json", "r") as file:
            paychecks_data = json.load(file)
        
        # Check if there is data in the file
        if not paychecks_data:
            return jsonify({"error": "No payroll data available"}), 404
        
        return jsonify(paychecks_data), 200
    except json.JSONDecodeError:
        return jsonify({"error": "Failed to decode JSON data"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Route to get payroll summary (total payroll, num employees, avg paycheck)
@app.route("/payroll", methods=["GET"])
def get_payroll():
    try:
        # Check if the file exists before attempting to open it
        if not os.path.exists("output/paychecks.json"):
            return jsonify({"error": "Payroll data file not found"}), 404
        
        with open("output/paychecks.json", "r") as file:
            paychecks_data = json.load(file)
        
        # Check if there is data in the file
        if not paychecks_data:
            return jsonify({"error": "No payroll data available"}), 404
        
        total_payroll = sum(paycheck["amount"] for paycheck in paychecks_data)
        num_employees = len(paychecks_data)
        average_paycheck = total_payroll / num_employees if num_employees else 0
        
        payroll_info = {
            "total_payroll": total_payroll,
            "num_employees": num_employees,
            "average_paycheck": average_paycheck
        }
        
        return jsonify(payroll_info), 200
    except json.JSONDecodeError:
        return jsonify({"error": "Failed to decode JSON data"}), 500
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

