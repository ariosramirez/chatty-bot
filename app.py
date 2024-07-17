from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__)


@app.route("/")
def index():
    return send_from_directory('static', 'index.html')

@app.route("/hello")
def hello_world():
    return "<p>Hello, World! Andy</p>"


@app.route("/chat", methods=["POST", "GET"])
def chat():
    user_message = request.json.get("message")
    rasa_server = os.getenv("RASA_SERVER", "http://localhost:5005")
    response = requests.post(
        f"{rasa_server}/webhooks/rest/webhook",
        json={"sender": "user", "message": user_message}
    )
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
