import random

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data to simulate contract numbers
# Contract numbers from "1" to "100"
contracts = [str(i) for i in range(1, 120)]


def calculate_credit_history(contract_number):
    """Simulate credit history calculation"""
    # Generate random values for the sake of example
    credit_score = random.randint(300, 850)
    debt_ratio = random.random()

    # Dummy logic for mortgage cancellation check
    if credit_score > 700 and debt_ratio < 0.3:
        return 'Go'
    elif credit_score > 600:
        return 'Orange'
    else:
        return 'Red'


@app.route('/check_mortgage_cancellation/<contract_number>', methods=['GET'])
def check_mortgage_cancellation(contract_number):
    # Check if the contract number exists
    if contract_number in contracts:
        # Calculate credit history and decide if the mortgage can be cancelled
        result = calculate_credit_history(contract_number)
        return jsonify({"contract_number": contract_number, "result": result})
    else:
        # Contract number doesn't exist
        return jsonify({"contract_number": contract_number, "result": "Red"})


if __name__ == "__main__":
    app.run(debug=True)
