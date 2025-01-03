from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    """Handle predictions."""
    data = request.json
    try:
        # Dummy model: Calculate a simple score based on input
        score = data["temperature"] * 0.5 + data["humidity"] * 0.3
        return jsonify({"prediction": score})
    except KeyError:
        return jsonify({"error": "Invalid input data"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
