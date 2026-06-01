from nl_to_sql import question_to_sql
from query_runner import run_query

question = input(
    "Ask a question: "
)

sql = question_to_sql(
    question
)

if sql:

    print("\nGenerated SQL:")
    print(sql)

    result = run_query(sql)

    print("\nResult:")
    print(result)

else:

    print(
        "Question not supported."
    )