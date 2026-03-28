from flask import Flask,request, jsonify
import requests

app = Flask(__name__)
API_KEY_A = "servicea-secret-key"
API_KEY_B = "serviceb-secret-key"

@app.route('/call_service_b', methods=['GET'])
def call_service_b():
    # Authenticate client
    client_api_key = request.headers.get('X-API-KEY')
    if client_api_key != API_KEY_A:
        return jsonify({"error": "Unauthorized"}), 401

    # Call ServiceB with ServiceA's API key
    headers = {"X-API-KEY": API_KEY_B}
    response = requests.get("http://localhost:5001/data", headers=headers)
    return jsonify({
        "service_b_response": response.json(),
        "status_code": response.status_code
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)