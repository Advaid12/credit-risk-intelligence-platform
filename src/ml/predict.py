import joblib

def get_risk_band(probability):

    score = probability * 100

    if score < 30:
        return score, "Low"

    elif score < 70:
        return score, "Medium"

    else:
        return score, "High"


model = joblib.load("models/model.pkl")

print("Model loaded successfully")
