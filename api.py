from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

BITRIX_WEBHOOK_URL = "https://drnda.bitrix24.com/rest/21/adcfj51t9r02r9oi/im.message.add.json"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    print("Primljen webhook:", data)  # Log za debagovanje

    # Ako je event ONIMBOTMESSAGEADD
    if data.get("event") == "ONIMBOTMESSAGEADD":
        dialog_id = data["data"].get("DIALOG_ID")
        user_message = data["data"].get("MESSAGE")

        # Formiranje odgovora
        response_message = f"Bot: Primio sam tvoju poruku - {user_message}"

        # Slanje odgovora u Bitrix chat
        payload = {
            "DIALOG_ID": dialog_id,
            "MESSAGE": response_message
        }
        response = requests.post(BITRIX_WEBHOOK_URL, json=payload)

        return jsonify({"status": "ok", "bitrix_response": response.json()})

    return jsonify({"status": "ok", "message": "Hello from Vercel!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
