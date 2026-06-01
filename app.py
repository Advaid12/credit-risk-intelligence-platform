import streamlit as st

from src.talk_to_data.nl_to_sql import question_to_sql
from src.talk_to_data.query_runner import run_query

st.set_page_config(
    page_title="Credit Risk Intelligence Platform",
    layout="wide"
)

st.title("🏦 Credit Risk Intelligence Platform")

tab1, tab2, tab3 = st.tabs(
    [
        "EDA Dashboard",
        "ML Results",
        "Talk To Data"
    ]
)

# ==========================
# TAB 1 - EDA
# ==========================
with tab1:

    st.header("Exploratory Data Analysis")

    st.image(
        "charts/default_distribution.png",
        caption="Loan Default Distribution"
    )

    st.image(
        "charts/income_distribution.png",
        caption="Income Distribution"
    )

    st.image(
        "charts/credit_distribution.png",
        caption="Credit Distribution"
    )

    st.image(
        "charts/shap_summary.png",
        caption="SHAP Explainability"
    )

# ==========================
# TAB 2 - ML Results
# ==========================
with tab2:

    st.header("Model Performance")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Accuracy", "0.9193")
        st.metric("Precision", "0.5625")

    with col2:
        st.metric("Recall", "0.0036")
        st.metric("ROC-AUC", "0.7256")

    st.success(
        "Random Forest Model Trained Successfully"
    )

# ==========================
# TAB 3 - Chatbot
# ==========================
with tab3:

    st.header("Talk To Data")

    question = st.text_input(
        "Ask a question"
    )

    if st.button("Submit"):

        sql = question_to_sql(question)

        if sql:

            result = run_query(sql)

            st.subheader("Generated SQL")
            st.code(sql)

            st.subheader("Result")
            if result:
                answer=result[0][0]
                st.success(f"Answer: {answer}")
            else:
                st.warning("No results found.")

        else:

            st.error(
                "Question not supported."
            )
