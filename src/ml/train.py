import sys
import os

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

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

import joblib

# -----------------------------
# Load Data
# -----------------------------
df = load_data()

# -----------------------------
# Preprocess
# -----------------------------
df = preprocess_data(df)

# -----------------------------
# Features and Target
# -----------------------------
X = df.drop("TARGET", axis=1)
y = df["TARGET"]

# -----------------------------
# Train Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# -----------------------------
# Model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced",
    n_jobs=-1
)

print("Training model...")

model.fit(X_train, y_train)

print("Training completed.")

# -----------------------------
# Predictions
# -----------------------------
y_pred = model.predict(X_test)

y_prob = model.predict_proba(X_test)[:, 1]

# -----------------------------
# Metrics
# -----------------------------
print("\nModel Evaluation")

print(
    "Accuracy:",
    round(accuracy_score(y_test, y_pred), 4)
)

print(
    "Precision:",
    round(precision_score(y_test, y_pred), 4)
)

print(
    "Recall:",
    round(recall_score(y_test, y_pred), 4)
)

print(
    "F1 Score:",
    round(f1_score(y_test, y_pred), 4)
)

print(
    "ROC AUC:",
    round(roc_auc_score(y_test, y_prob), 4)
)

# -----------------------------
# Save Model
# -----------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(
    model,
    "models/model.pkl"
)

print(
    "\nModel saved to models/model.pkl"
)
