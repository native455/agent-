def add(a, b):
    return float(a) + float(b)


def subtract(a, b):
    return float(a) - float(b)


def multiply(a, b):
    return float(a) * float(b)


def divide(a, b):

    if float(b) == 0:
        return "Cannot divide by zero."

    return float(a) / float(b)


TOOLS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}
