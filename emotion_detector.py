def detect_emotion(text: str) -> str:
    text = text.lower()

    patterns = {
        "greeting": ["hi", "hello", "hey", "assalam", "salam"],
        "goodbye": ["bye", "good night", "see you", "take care"],
        "sadness": ["sad", "down", "cry", "hurt", "tears"],
        "anger": ["angry", "mad", "furious", "rage"],
        "stress": ["stress", "pressure", "burden"],
        "depression": ["depressed", "empty", "hopeless"],
        "anxiety": ["anxious", "nervous", "worried"],
        "panic": ["panic", "heart racing", "can't breathe"],
        "lonely": ["lonely", "alone", "nobody"],
        "overwhelmed": ["overwhelmed", "too much", "breaking"],
        "broken": ["broken", "shattered", "damaged"],
        "emotionally_unstable": ["unstable", "losing control"],
        "happiness": ["happy", "grateful", "good today"],
        "excitement": ["excited", "thrilled", "can't wait"]
    }

    for emotion, keywords in patterns.items():
        if any(k in text for k in keywords):
            return emotion

    return "neutral"