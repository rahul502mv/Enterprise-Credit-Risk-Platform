import streamlit as st
import matplotlib.pyplot as plt


# ---------------------------------------
# Risk Category Distribution
# ---------------------------------------

def risk_distribution_chart(results):

    st.subheader("📊 Risk Category Distribution")

    risk_counts = results[
        "Risk Category"
    ].value_counts()

    fig, ax = plt.subplots(
        figsize=(6, 4)
    )

    ax.bar(
        risk_counts.index,
        risk_counts.values
    )

    ax.set_xlabel(
        "Risk Category"
    )

    ax.set_ylabel(
        "Customers"
    )

    ax.set_title(
        "Loan Risk Distribution"
    )

    st.pyplot(fig)


# ---------------------------------------
# Default Probability Histogram
# ---------------------------------------

def probability_distribution(results):

    st.subheader(
        "📈 Default Probability Distribution"
    )

    fig, ax = plt.subplots(
        figsize=(6, 4)
    )

    ax.hist(
        results["Default Probability"],
        bins=20
    )

    ax.set_xlabel(
        "Default Probability"
    )

    ax.set_ylabel(
        "Customers"
    )

    ax.set_title(
        "Default Probability Histogram"
    )

    st.pyplot(fig)