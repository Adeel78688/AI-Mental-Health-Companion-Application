from flask import Flask, request, jsonify
from groq import Groq

from config import GROQ_API_KEY
from emergency_detector import detect_crisis
from memory_store import MemoryStore

app = Flask(__name__)

client = Groq(api_key=GROQ_API_KEY)
memory = MemoryStore()

SYSTEM_PROMPT = (
    "You are a calm, empathetic emotional support assistant. "
    "Respond with care, validation, and emotional awareness. "
    "Keep replies concise and supportive."
)


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "✅ Flask server is running and reachable."})


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "").strip()
    user_id = data.get("user_id", "default_user")

    if not user_input:
        return jsonify({"error": "Empty message"}), 400

    # Crisis detection
    if detect_crisis(user_input):
        return jsonify({
            "emotion": "crisis",
            "response": (
                "🚨 It sounds like you may be in crisis. "
                "Please reach out to a trusted person or local helpline immediately."
            )
        })

    # Store user message
    memory.update_context(user_id, user_input, role="user")
    context = memory.get_context(user_id)

    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    for m in context[-5:]:
        role = "user" if m["role"] == "user" else "assistant"
        messages.append({"role": role, "content": m["content"]})

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            temperature=0.6,
            max_tokens=200
        )

        bot_reply = response.choices[0].message.content.strip()
        memory.update_context(user_id, bot_reply, role="model")

    except Exception:
        bot_reply = (
            "I'm here with you, but something went wrong on my side. "
            "Please try again in a moment."
        )

    return jsonify({
        "emotion": "supportive",
        "response": bot_reply
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)