
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
X_text = vectorizer.fit_transform(df['Comments'])
