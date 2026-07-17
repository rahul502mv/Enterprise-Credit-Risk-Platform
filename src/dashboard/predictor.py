import joblib
import pandas as pd

from src.utils.config import MODEL_PATH


# ---------------------------------------
# Load Saved Artifacts
# ---------------------------------------

model = joblib.load(
    MODEL_PATH / "lightgbm_model.pkl"
)

imputer = joblib.load(
    MODEL_PATH / "imputer.pkl"
)

scaler = joblib.load(
    MODEL_PATH / "scaler.pkl"
)

feature_columns = joblib.load(
    MODEL_PATH / "feature_columns.pkl"
)


# ---------------------------------------
# Risk Category
# ---------------------------------------

def risk_category(probability):

    if probability < 0.20:
        return "Low Risk"

    elif probability < 0.50:
        return "Medium Risk"

    else:
        return "High Risk"


# ---------------------------------------
# Recommendation
# ---------------------------------------

def recommendation(risk):

    if risk == "Low Risk":
        return "Approve Loan"

    elif risk == "Medium Risk":
        return "Manual Review"

    else:
        return "Reject / Investigate"


# ---------------------------------------
# Prediction Function
# ---------------------------------------

def predict_dataset(df):

    X = df.copy()

    drop_columns = []

    if "SK_ID_CURR" in X.columns:
        drop_columns.append("SK_ID_CURR")

    if "TARGET" in X.columns:
        drop_columns.append("TARGET")

    X = X.drop(
        columns=drop_columns
    )

    X = X.select_dtypes(
        include="number"
    )

    X = X[
        feature_columns
    ]

    X = imputer.transform(
        X
    )

    X = scaler.transform(
        X
    )

    prediction = model.predict(
        X
    )

    probability = model.predict_proba(
        X
    )[:, 1]

    results = df.copy()

    results["Prediction"] = prediction

    results["Default Probability"] = probability

    results["Risk Category"] = results[
        "Default Probability"
    ].apply(
        risk_category
    )

    results["Recommendation"] = results[
        "Risk Category"
    ].apply(
        recommendation
    )

    return results