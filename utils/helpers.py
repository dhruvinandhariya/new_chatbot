def format_chat_history(history, max_length=1000):
    history_text = []
    for msg in history[-6:]:
        role = "User" if msg["role"] == "user" else "Assistant"
        history_text.append(f"{role}: {msg['content']}")
    return "\n".join(history_text)[:max_length]

def generate_response_hash(response):
    import hashlib
    return hashlib.md5(response.encode()).hexdigest()