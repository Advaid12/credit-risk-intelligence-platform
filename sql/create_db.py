import pandas as pd
import sqlite3

# Load dataset
df = pd.read_csv("data/application_train.csv")

# Create database
conn = sqlite3.connect("sql/credit_risk.db")

# Save table
df.to_sql(
    "customers",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database created successfully")
