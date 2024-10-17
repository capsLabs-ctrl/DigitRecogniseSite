from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from predict import predict, editArray
app = Flask(__name__)
CORS(app, origins=["http://127.0.0.1:5500"])
@app.route('/')
def home():
    return "Welcome to the Flask app!"

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json
    predictions, predictedclass = predict(data, 'my_model.keras')
    result = {"status": "ok", "processed_data": data, "predicted value": predictedclass}
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)