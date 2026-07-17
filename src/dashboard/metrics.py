import streamlit as st


# ---------------------------------------
# Dashboard Metrics
# ---------------------------------------

def show_metrics(results):

    total_customers = len(results)

    high_risk = (
        results["Risk Category"] == "High Risk"
    ).sum()

    medium_risk = (
        results["Risk Category"] == "Medium Risk"
    ).sum()

    low_risk = (
        results["Risk Category"] == "Low Risk"
    ).sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "👥 Customers",
        total_customers
    )

    col2.metric(
        "🔴 High Risk",
        high_risk
    )

    col3.metric(
        "🟡 Medium Risk",
        medium_risk
    )

    col4.metric(
        "🟢 Low Risk",
        low_risk
    )