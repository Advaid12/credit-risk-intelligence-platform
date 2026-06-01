def question_to_sql(question):

    question = question.lower()

    mapping = {

        "how many customers defaulted":
        """
        SELECT COUNT(*)
        FROM customers
        WHERE TARGET = 1
        """,

        "average income":
        """
        SELECT AVG(AMT_INCOME_TOTAL)
        FROM customers
        """,

        "average credit amount":
        """
        SELECT AVG(AMT_CREDIT)
        FROM customers
        """,

        "default rate":
        """
        SELECT
        ROUND(
            AVG(TARGET) * 100,
            2
        )
        FROM customers
        """,

        "most common education type":
        """
        SELECT
        NAME_EDUCATION_TYPE,
        COUNT(*)
        FROM customers
        GROUP BY NAME_EDUCATION_TYPE
        ORDER BY COUNT(*) DESC
        LIMIT 1
        """
    }

    for key in mapping:

        if key in question:

            return mapping[key]

    return None
