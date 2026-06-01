import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------
# Create charts directory
# -----------------------------
os.makedirs("charts", exist_ok=True)

# -----------------------------
# Load Dataset
# -----------------------------
print("\nLoading dataset...")

df = pd.read_csv("data/application_train.csv")

print("Dataset Loaded Successfully!")

# -----------------------------
# Dataset Overview
# -----------------------------
print("\n" + "=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print(f"\nRows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nFirst 5 Rows:")
print(df.head())

# -----------------------------
# Data Types
# -----------------------------
print("\n" + "=" * 60)
print("DATA TYPES")
print("=" * 60)

print(df.dtypes.value_counts())

# -----------------------------
# Feature Categorization
# -----------------------------
categorical_cols = df.select_dtypes(include=["object"]).columns
numerical_cols = df.select_dtypes(exclude=["object"]).columns

print("\n" + "=" * 60)
print("FEATURE CATEGORIZATION")
print("=" * 60)

print(f"Categorical Features: {len(categorical_cols)}")
print(f"Numerical Features: {len(numerical_cols)}")

# -----------------------------
# Missing Values Analysis
# -----------------------------
print("\n" + "=" * 60)
print("TOP 20 MISSING VALUE COLUMNS")
print("=" * 60)

missing_values = df.isnull().sum()
missing_percentage = (missing_values / len(df)) * 100

missing_df = pd.DataFrame({
    "Missing Count": missing_values,
    "Missing %": missing_percentage
})

missing_df = missing_df.sort_values(
    by="Missing %",
    ascending=False
)

print(missing_df.head(20))

# Save Missing Values Report
missing_df.to_csv(
    "charts/missing_values_report.csv"
)

# -----------------------------
# Target Distribution
# -----------------------------
print("\n" + "=" * 60)
print("TARGET DISTRIBUTION")
print("=" * 60)

print(df["TARGET"].value_counts())

print("\nPercentage Distribution")

print(
    df["TARGET"]
    .value_counts(normalize=True) * 100
)

# -----------------------------
# Chart 1
# Default Distribution
# -----------------------------
plt.figure(figsize=(6, 4))

sns.countplot(
    x="TARGET",
    data=df
)

plt.title("Loan Default Distribution")

plt.savefig(
    "charts/default_distribution.png",
    bbox_inches="tight"
)

plt.close()

# -----------------------------
# Chart 2
# Income Distribution
# -----------------------------
plt.figure(figsize=(8, 5))

sns.histplot(
    df["AMT_INCOME_TOTAL"],
    bins=50
)

plt.title("Income Distribution")

plt.savefig(
    "charts/income_distribution.png",
    bbox_inches="tight"
)

plt.close()

# -----------------------------
# Chart 3
# Credit Amount Distribution
# -----------------------------
plt.figure(figsize=(8, 5))

sns.histplot(
    df["AMT_CREDIT"],
    bins=50
)

plt.title("Credit Amount Distribution")

plt.savefig(
    "charts/credit_distribution.png",
    bbox_inches="tight"
)

plt.close()

# -----------------------------
# Chart 4
# Gender Distribution
# -----------------------------
plt.figure(figsize=(6, 4))

sns.countplot(
    x="CODE_GENDER",
    data=df
)

plt.title("Gender Distribution")

plt.savefig(
    "charts/gender_distribution.png",
    bbox_inches="tight"
)

plt.close()

# -----------------------------
# Chart 5
# Education Type Distribution
# -----------------------------
plt.figure(figsize=(10, 5))

sns.countplot(
    y="NAME_EDUCATION_TYPE",
    data=df,
    order=df["NAME_EDUCATION_TYPE"]
    .value_counts()
    .index
)

plt.title("Education Type Distribution")

plt.savefig(
    "charts/education_distribution.png",
    bbox_inches="tight"
)

plt.close()

# -----------------------------
# Correlation Heatmap
# -----------------------------
plt.figure(figsize=(10, 8))

corr_columns = [
    "TARGET",
    "AMT_INCOME_TOTAL",
    "AMT_CREDIT",
    "AMT_ANNUITY"
]

corr_matrix = df[corr_columns].corr()

sns.heatmap(
    corr_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.savefig(
    "charts/correlation_heatmap.png",
    bbox_inches="tight"
)

plt.close()

# -----------------------------
# Business Insights
# -----------------------------
print("\n" + "=" * 60)
print("BUSINESS INSIGHTS")
print("=" * 60)

default_rate = (
    df["TARGET"].mean() * 100
)

print(
    f"\n1. Default Rate: "
    f"{default_rate:.2f}%"
)

avg_income = (
    df["AMT_INCOME_TOTAL"]
    .mean()
)

print(
    f"\n2. Average Income: "
    f"{avg_income:,.2f}"
)

avg_credit = (
    df["AMT_CREDIT"]
    .mean()
)

print(
    f"\n3. Average Credit Amount: "
    f"{avg_credit:,.2f}"
)

print(
    "\n4. Dataset contains "
    "significant missing values "
    "that require preprocessing."
)

print(
    "\n5. Dataset is highly "
    "imbalanced because "
    "non-default customers "
    "significantly outnumber "
    "default customers."
)

print("\nEDA Completed Successfully!")

print(
    "\nCharts saved inside "
    "'charts/' folder."
)