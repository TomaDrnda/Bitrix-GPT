from flask import Flask, request, jsonify 
app = Flask(__name__) 
@app.route("/webhook", methods=["POST"]) 
def webhook(): 
    data = request.json 
    print("Received data:", data) 
    return jsonify({"status": "ok", "message": "Hello from Vercel!"}) 
if __name__ == "__main__": 
    app.run() 
