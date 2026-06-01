Here's a **professional README.md** tailored to your NeoStats Credit Risk Intelligence Platform assignment.

---

# 🏦 Credit Risk Intelligence Platform

An end-to-end AI-powered Credit Risk Intelligence Platform built using Machine Learning, Explainable AI, Natural Language to SQL, Streamlit, and Docker.

The platform analyzes customer credit data, predicts loan default risk, provides explainable insights using SHAP, and allows business users to query data using natural language.

---

# 🚀 Features

### 📊 Exploratory Data Analysis (EDA)

* Dataset overview and feature categorization
* Missing value analysis
* Business insights generation
* Visualizations:

  * Loan Default Distribution
  * Income Distribution
  * Credit Distribution
  * Education Distribution
  * Gender Distribution
  * Correlation Heatmap

---

### 🤖 Machine Learning Layer

* Data preprocessing pipeline
* Missing value handling
* Categorical feature encoding
* Random Forest Classifier
* Class imbalance handling using class weights

#### Model Metrics

| Metric    | Value  |
| --------- | ------ |
| Accuracy  | 0.9193 |
| Precision | 0.5625 |
| Recall    | 0.0036 |
| F1 Score  | 0.0072 |
| ROC-AUC   | 0.7256 |

---

### 🔍 Explainable AI

SHAP (SHapley Additive exPlanations) was used to interpret model predictions.

Top influencing features:

* EXT_SOURCE_2
* EXT_SOURCE_3
* DAYS_BIRTH
* EXT_SOURCE_1
* DAYS_ID_PUBLISH
* AMT_ANNUITY
* DAYS_EMPLOYED
* AMT_CREDIT

---

### 💬 Talk To Data (NL → SQL)

Users can ask business questions in natural language.

Examples:

#### Example 1

**Question**

```text
How many customers defaulted?
```

**Generated SQL**

```sql
SELECT COUNT(*)
FROM customers
WHERE TARGET = 1;
```

**Result**

```text
24825
```

---

#### Example 2

**Question**

```text
average income
```

**Result**

```text
168797.92
```

---

#### Example 3

```text
average credit amount
```

---

#### Example 4

```text
default rate
```

---

#### Example 5

```text
most common education type
```

---

### 🌐 Streamlit Dashboard

The platform provides a unified UI containing:

* EDA Dashboard
* ML Results Dashboard
* Explainability Dashboard
* Talk To Data Chatbot

---

# 🏗️ Project Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ├── EDA Dashboard
 │
 ├── ML Layer
 │      │
 │      ▼
 │   Random Forest Model
 │
 ├── SHAP Explainability
 │
 └── NL → SQL Chatbot
         │
         ▼
      SQLite Database
```

---

# 📂 Project Structure

```text
credit_risk_platform/

├── data/
├── documents/
├── notebooks/
│   └── eda.py
│
├── src/
│   ├── data/
│   │   ├── loader.py
│   │   └── preprocessor.py
│   │
│   ├── ml/
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   └── explain.py
│   │
│   ├── talk_to_data/
│   │   ├── nl_to_sql.py
│   │   ├── query_runner.py
│   │   └── prompt_templates.py
│   │
│   └── utils/
│
├── sql/
│   ├── create_db.py
│   └── schema.sql
│
├── charts/
├── models/
├── Dockerfile
├── docker-compose.yml
├── app.py
├── requirements.txt
└── README.md
```

---

# 📈 Dataset

Dataset used:

**Home Credit Default Risk Dataset**

Source:

```text
https://www.kaggle.com/competitions/home-credit-default-risk
```

Required files:

```text
application_train.csv
application_test.csv
```

Place them inside:

```text
data/
```

---

# ⚙️ Installation

# ▶️ Running the Project

## Generate Database

```bash
python sql/create_db.py
```

---

## Train Model

```bash
python src/ml/train.py
```

---

## Launch Streamlit

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# 🐳 Docker

Build image:

```bash
docker build -t credit-risk-platform .
```

Run container:

```bash
docker run -p 8501:8501 credit-risk-platform
```

---

# 📸 Screenshots

Add screenshots of:

* EDA Dashboard
* ML Results
* SHAP Explainability
* NL → SQL Chatbot

inside:

```text
documents/screenshots/
```

---

# 🔮 Future Improvements

* XGBoost / LightGBM implementation
* SMOTE for class imbalance
* LLM-powered dynamic NL → SQL generation
* Real-time model monitoring
* Advanced risk segmentation
* Cloud deployment

---

# 👨‍💻 Author

**Advaith Manoj**

B.Tech Computer Science & Engineering

Credit Risk Intelligence Platform – NeoStats AI Engineering Assignment

---
