
def add_numbers(a, b):
    return int(a) + int(b)  # Convert inputs to integers to prevent TypeError

result = add_numbers("10", 5)  # Now works correctly
print("Result:", result)
