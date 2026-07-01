from core.memory import memory


def remember(key, value):
    memory.remember(key, value)
    return f"I'll remember that {key} = {value}"


def recall(key):

    value = memory.recall(key)

    if value is None:
        return "I don't know."

    return value


def forget(key):

    memory.forget(key)

    return f"Forgot {key}."


def show_memory():

    return memory.all()
