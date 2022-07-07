import joblib

model = joblib.load('regression')

print(model.coef_)

print(model.predict([[1.4]]))
