
# Code with error:
def divide(a, b):
    return a / b

# AI suggestion: Handle division by zero
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
