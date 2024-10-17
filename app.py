from flask import Flask, request, jsonify
import os
from predict import predict, editArray
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask app!"

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json
    data = editArray(data)
    predictions, predictedclass = predict(data)
    result = {"status": "ok", "processed_data": data, "predicted value": predictedclass}
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)