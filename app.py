from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.json
    # Здесь будет код обработки массива
    result = {"status": "ok", "processed_data": data}
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)