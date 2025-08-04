
with open('file.txt', 'r') as file:
    text = file.read()
    words = text.split()
    print(f"Word count: {len(words)}")
