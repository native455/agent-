from tinydb import TinyDB

db = TinyDB("memory.json")

def remember(user, ai):
    db.insert({
        "user": user,
        "ai": ai
    })

def recall(limit=5):
    return db.all()[-limit:]
