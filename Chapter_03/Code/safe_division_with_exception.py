
def divide(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

# Example usage
try:
    print(divide(10, 0))
except ValueError as e:
    print("Caught an error:", e)
