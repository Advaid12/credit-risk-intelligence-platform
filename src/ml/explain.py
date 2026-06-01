import os
import sys
import joblib
import shap
import matplotlib.pyplot as plt

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "data"
        )
    )
)

from loader import load_data
from preprocessor import preprocess_data

# Load data
df = load_data()
df = preprocess_data(df)

# Features only
X = df.drop("TARGET", axis=1)

# Load trained model
model = joblib.load("models/model.pkl")

print("Generating SHAP explanations...")

# SHAP Explainer
explainer = shap.TreeExplainer(model)

# Sample data (faster)
X_sample = X.sample(50, random_state=42)

shap_values = explainer.shap_values(X_sample)

# Create folder
os.makedirs("charts", exist_ok=True)

# Summary Plot
shap.summary_plot(
    shap_values[:, :, 1] if len(shap_values.shape) == 3 else shap_values,
    X_sample,
    show=False
)

plt.savefig(
    "charts/shap_summary.png",
    bbox_inches="tight"
)

plt.close()

print("SHAP summary plot saved.")
