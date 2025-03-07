from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Received data:", data)
    return jsonify({"status": "ok", "message": "Hello from Vercel!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
