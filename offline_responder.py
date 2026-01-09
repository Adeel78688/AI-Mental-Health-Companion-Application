import random

RESPONSES = {
    "greeting": [
        "Hey, I'm really glad you reached out today. How are you feeling right now?",
        "Hello 🌱 I'm here with you. What's been on your mind lately?"
    ],

    "goodbye": [
        "Take care of yourself. If things feel heavy again, I'll be right here.",
        "You don't have to handle everything alone. Come back whenever you need."
    ],

    "sadness": [
        "That sounds really painful. I'm sorry you're going through this. What happened?",
        "I can hear how heavy this feels for you. Want to tell me more about it?"
    ],

    "anger": [
        "It sounds like something really crossed a line for you. What made you feel this way?",
        "Anger often comes from hurt. What do you think triggered this?"
    ],

    "stress": [
        "You've been carrying a lot. Let's slow down for a moment — what's weighing on you most?",
        "It feels overwhelming when everything piles up. Where do you want to start?"
    ],

    "depression": [
        "Feeling empty like this can be exhausting. I'm really glad you spoke up.",
        "When did this feeling start? I want to understand it with you."
    ],

    "anxiety": [
        "That constant worry can be draining. What's your mind stuck on right now?",
        "Let's take this one step at a time. What's making you anxious today?"
    ],

    "panic": [
        "I'm here with you. Let's slow your breathing together for a moment.",
        "You're safe right now. Can you tell me what you were thinking just before this started?"
    ],

    "lonely": [
        "Feeling alone can hurt deeply. What's been making you feel disconnected?",
        "I'm really glad you reached out. When did this loneliness start feeling heavy?"
    ],

    "overwhelmed": [
        "It sounds like everything hit you at once. What feels like the hardest part?",
        "You don't have to solve everything right now. What's one thing that's bothering you?"
    ],

    "broken": [
        "Feeling broken can make everything feel hopeless. What made you feel this way?",
        "That sounds deeply painful. What happened that hurt you like this?"
    ],

    "emotionally_unstable": [
        "It sounds like your emotions are all over the place. That can be scary.",
        "Let's ground ourselves for a moment. What are you feeling right now?"
    ],

    "happiness": [
        "That's really nice to hear 😊 What's been going well for you?",
        "I'm glad you're feeling good today. Want to share what made you feel this way?"
    ],

    "excitement": [
        "That sounds exciting! What are you most looking forward to?",
        "I love hearing that energy — tell me more about it!"
    ],

    "neutral": [
        "I'm here and listening. What's been on your mind lately?",
        "You can talk freely here. What would you like to share?"
    ]
}


def get_offline_reply(emotion: str) -> str:
    return random.choice(RESPONSES.get(emotion, RESPONSES["neutral"]))
