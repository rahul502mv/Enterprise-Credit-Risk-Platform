import streamlit as st
import pandas as pd

from src.dashboard.predictor import predict_dataset
from src.dashboard.metrics import show_metrics
from src.dashboard.charts import (
    risk_distribution_chart,
    probability_distribution
)

# ---------------------------------------
# Page Configuration
# ---------------------------------------

st.set_page_config(
    page_title="Enterprise Credit Risk Platform",
    page_icon="🏦",
    layout="wide"
)

# ---------------------------------------
# Title
# ---------------------------------------

st.title(
    "🏦 Enterprise AI-Powered Credit Risk Intelligence Platform"
)

st.markdown(
    """
Predict customer loan default risk using the trained
LightGBM model.
"""
)

st.divider()

# ---------------------------------------
# Upload Dataset
# ---------------------------------------

uploaded_file = st.file_uploader(
    "📂 Upload Customer Dataset (CSV)",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("📋 Dataset Preview")

    st.dataframe(
        df.head()
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "Rows",
        df.shape[0]
    )

    col2.metric(
        "Columns",
        df.shape[1]
    )

    st.divider()

    if st.button(
        "🚀 Predict Loan Default",
        use_container_width=True
    ):

        with st.spinner(
            "Running Prediction..."
        ):

            try:

                results = predict_dataset(df)

                st.success(
                    "Prediction Completed Successfully!"
                )

                st.divider()

                # --------------------------
                # KPI Cards
                # --------------------------

                st.subheader(
                    "📊 Dashboard Summary"
                )

                show_metrics(
                    results
                )

                st.divider()

                # --------------------------
                # Charts
                # --------------------------

                risk_distribution_chart(
                    results
                )

                probability_distribution(
                    results
                )

                st.divider()

                # --------------------------
                # Business Results
                # --------------------------

                st.subheader(
                    "📋 Prediction Results"
                )

                display_columns = [

                    "SK_ID_CURR",

                    "Prediction",

                    "Default Probability",

                    "Risk Category",

                    "Recommendation"

                ]

                available_columns = [

                    col

                    for col in display_columns

                    if col in results.columns

                ]

                st.dataframe(

                    results[
                        available_columns
                    ]

                )

                st.download_button(

                    label="📥 Download Prediction Results",

                    data=results.to_csv(
                        index=False
                    ),

                    file_name="credit_risk_predictions.csv",

                    mime="text/csv"

                )

            except Exception as e:

                st.error(

                    f"Prediction Failed : {e}"

                )

else:

    st.info(
        "Please upload application_train_sample.csv to begin prediction."
    )