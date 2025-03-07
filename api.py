from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return jsonify({"status": "ok", "message": "Webhook endpoint is working!"})

    if request.method == "POST":
        data = request.json
        print("Received data:", data)
        return jsonify({"status": "ok", "message": "Hello from Vercel!"})

if __name__ == "__main__":
    app.run(debug=True)
