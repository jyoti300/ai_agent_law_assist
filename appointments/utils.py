def is_booking_intent(text):
    words = ["book", "appointment", "meeting", "schedule"]
    return any(w in text.lower() for w in words)
