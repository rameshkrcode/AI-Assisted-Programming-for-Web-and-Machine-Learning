
# AI-suggested code might miss edge cases
def divide(a, b):
    return a / b

# Safer, developer-reviewed version
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
