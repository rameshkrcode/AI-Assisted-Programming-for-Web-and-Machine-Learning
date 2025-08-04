
# Original code:
result = []
for i in range(len(data)):
    result.append(data[i] * 2)

# Suggested optimization:
result = [x * 2 for x in data]
