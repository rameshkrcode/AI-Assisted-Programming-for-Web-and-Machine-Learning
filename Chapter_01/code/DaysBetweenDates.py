# AI-assisted function suggestion
from datetime import datetime
def calculate_days_between_dates(date1, date2):
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    return abs((d2 - d1).days)
# Suggestion by AI tools like GitHub Copilot
print(calculate_days_between_dates('2025-01-01', '2025-01-10'))
