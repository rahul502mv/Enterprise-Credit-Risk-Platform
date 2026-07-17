import pandas as pd

from src.models.load_model import load_artifacts


model, imputer, scaler = load_artifacts()


def predict_customer(

    data: pd.DataFrame

):

    data = imputer.transform(data)

    data = scaler.transform(data)

    prediction = model.predict(data)

    probability = model.predict_proba(data)[:, 1]

    return prediction, probability