
def calculate_average(scores):
    if not scores:
        return "Error: Empty list"
    return sum(scores) / len(scores)
