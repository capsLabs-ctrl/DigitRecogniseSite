from flask import Flask, request, jsonify, render_template
from flask_cors import CORS 
import os
from predict import predict, editArray
app = Flask(__name__, static_folder='frontend')
CORS(app, origins=["http://127.0.0.1:5500"])
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json
    if data is None:
        return jsonify({"error": "No JSON received"}), 400
    predictions, predictedclass = predict(data["array"], 'cnn_model_15epoch.keras' if data["model"] == "cnn15e" else 'cnn_model_5epoch.keras' if data["model"] == "cnn5e" else "my_model.keras" if data["model"] == "perseptron" else "cnn_model_115e_wd.keras" if data["model"] == "cnn115wd" else "cnn_model_15e_wd.keras" )
    result = {"status": "ok", "processed_data": data, "predicted value": int(predictedclass[0]), "predictions" : predictions[0].tolist()}
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)