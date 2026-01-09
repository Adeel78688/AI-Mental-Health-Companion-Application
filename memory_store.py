class MemoryStore:
    def __init__(self):
        self.sessions = {}

    def get_context(self, user_id):
        return self.sessions.get(user_id, [])

    def update_context(self, user_id, message, role="user"):
        if user_id not in self.sessions:
            self.sessions[user_id] = []
        self.sessions[user_id].append({"role": role, "content": message})

    def clear(self, user_id):
        if user_id in self.sessions:
            del self.sessions[user_id]