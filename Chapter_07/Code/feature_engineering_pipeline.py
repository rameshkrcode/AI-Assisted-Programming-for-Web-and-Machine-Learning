
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.feature_selection import SelectKBest, f_regression
pipeline = Pipeline([
    ('poly', PolynomialFeatures(degree=2, include_bias=False)),
    ('select', SelectKBest(score_func=f_regression, k=2))
])
X_transformed = pipeline.fit_transform(X, y)
