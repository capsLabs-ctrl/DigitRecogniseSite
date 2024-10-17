from flask import Flask, request, jsonify
import os
app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json
    # Здесь будет код обработки массива
    result = {"status": "ok", "processed_data": data}
    return jsonify(result)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)