from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Telegram bot token
TELEGRAM_BOT_TOKEN = "8108932885:AAHmLikb9iXiI-8bsZBEyqC816yxwlYFlXI"
TELEGRAM_CHAT_ID = None  # Временно, будет определён динамически
SESSIONS = {}

@app.route("/send", methods=["POST"])
def send_message():
    data = request.get_json()
    message = data.get("message", "")
    session_id = data.get("session_id")

    if not message or not session_id:
        return jsonify({"error": "Missing message or session_id"}), 400

    SESSIONS[session_id] = None

    # Отправка сообщения в Telegram
    text = f"📩 Новое сообщение от пользователя #{session_id}:
{message}"
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID or "<YOUR_CHAT_ID>", "text": text}
    requests.post(url, json=payload)

    return jsonify({"status": "sent"}), 200

@app.route("/reply", methods=["POST"])
def reply_to_user():
    data = request.get_json()
    session_id = data.get("session_id")
    reply = data.get("reply")

    if not session_id or not reply:
        return jsonify({"error": "Missing session_id or reply"}), 400

    SESSIONS[session_id] = reply
    return jsonify({"status": "reply stored"}), 200

@app.route("/receive/<session_id>")
def get_reply(session_id):
    reply = SESSIONS.get(session_id)
    if reply:
        SESSIONS[session_id] = None  # Очистить после доставки
    return jsonify({"reply": reply})
