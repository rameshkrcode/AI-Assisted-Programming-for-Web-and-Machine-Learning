
# Input comment:
# Generate a Fibonacci sequence
def fibonacci(n):
    # AI-suggested implementation:
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence
print(fibonacci(10))
