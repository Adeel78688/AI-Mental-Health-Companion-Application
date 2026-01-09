from groq import Groq
from config import GROQ_API_KEY
from emergency_detector import detect_crisis
from memory_store import MemoryStore
import time
import sys

# Init Groq client
client = Groq(api_key=GROQ_API_KEY)

memory = MemoryStore()
print("Chatbot is ready. Type 'quit' to exit.\n")
user_id = "default_user"

CRISIS_RESPONSE = (
    "You're not alone. It sounds like you may be going through a really difficult time. "
    "Please consider talking to someone who can help right now:\n"
    "- Call or text a suicide prevention helpline in your country\n"
    "- In the US, call or text 988\n"
    "- In the UK, call Samaritans at 116 123\n"
    "- In Pakistan, call Umang at 0311 7786264\n"
    "If you can, please reach out to a trusted friend or family member."
)


def typing_animation(text="🤖 typing", delay=0.4, dots=3):
    for i in range(dots):
        sys.stdout.write("\r" + text + "." * (i + 1))
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\r" + " " * 30 + "\r")
    sys.stdout.flush()


SYSTEM_INSTRUCTION = (
    "You are a warm, empathetic emotional support chatbot created by Hassan Mohtashim. "
    "He is a Computer Science graduate, Android Developer, and AI/ML enthusiast. "
    "This chatbot is part of his FYP (AI-based Mental Health Companion Android app). "
    "Keep responses under 100 words. "
    "Respond empathetically, validate emotions, and ask gentle follow-up questions. "
    "Do NOT give harmful advice. "
    "If the user shows extreme emotional instability, suggest suitable CBT exercises. "
    "If user is in crisis, suggest professional help resources."
)


while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "quit":
        print("👋 Goodbye!")
        break

    # Crisis detection
    if detect_crisis(user_input):
        typing_animation()
        print("\n🚨 Emergency Alert Triggered!")
        print("🤖 Emotion: crisis")
        print(f"💬 Response: {CRISIS_RESPONSE}\n")
        continue

    # Store user message
    memory.update_context(user_id, user_input, role="user")
    context = memory.get_context(user_id)

    # Build Groq messages
    messages = [{"role": "system", "content": SYSTEM_INSTRUCTION}]

    for m in context[-5:]:
        role = "user" if m["role"] == "user" else "assistant"
        messages.append({"role": role, "content": m["content"]})

    typing_animation()

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages,
        temperature=0.6,
        max_tokens=180
    )

    bot_reply = response.choices[0].message.content.strip()
    print(f"🤖 {bot_reply}\n")

    # Store bot reply
    memory.update_context(user_id, bot_reply, role="model")
