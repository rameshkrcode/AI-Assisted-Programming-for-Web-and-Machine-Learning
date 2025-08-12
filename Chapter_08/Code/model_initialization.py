
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

model = RandomForestClassifier(class_weight='balanced', max_depth=10)
# Alternative:
# model = LogisticRegression(class_weight='balanced')
