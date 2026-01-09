CRISIS_KEYWORDS = [
    "suicide", "kill myself", "ending it all", "end my life",
    "I want to die", "no reason to live", "I'm done"
]

def detect_crisis(text):
    lowered = text.lower()
    return any(keyword in lowered for keyword in CRISIS_KEYWORDS)