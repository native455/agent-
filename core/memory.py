import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMORY_FILE = os.path.join(BASE_DIR, "data", "memory.json")


class MemoryManager:

    def __init__(self):
        self.memory = self.load()

    def load(self):

        if not os.path.exists(MEMORY_FILE):
            return {}

        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def save(self):

        os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(self.memory, f, indent=4)

    def remember(self, key, value):

        self.memory[key] = value
        self.save()

    def recall(self, key):

        return self.memory.get(key)

    def forget(self, key):

        if key in self.memory:
            del self.memory[key]
            self.save()

    def all(self):

        return self.memory


memory = MemoryManager()
