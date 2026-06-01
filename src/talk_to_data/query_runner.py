import sqlite3


def run_query(query):

    conn = sqlite3.connect(
        "sql/credit_risk.db"
    )

    cursor = conn.cursor()

    cursor.execute(query)

    result = cursor.fetchall()

    conn.close()

    return result
