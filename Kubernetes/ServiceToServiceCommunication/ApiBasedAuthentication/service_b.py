# service_b.py
from flask import Flask, request, jsonify

app = Flask(__name__)
API_KEY_B = "serviceb-secret-key"

@app.route('/data', methods=['GET'])
def get_data():
    api_key = request.headers.get('X-API-KEY')
    if api_key != API_KEY_B:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"data": "Protected data from ServiceB."})

if __name__ == '__main__':
    app.run(port=5001, debug=True)