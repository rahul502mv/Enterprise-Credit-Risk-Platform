import joblib

from src.utils.config import MODEL_PATH


def load_artifacts():

    model = joblib.load(

        MODEL_PATH / "lightgbm_model.pkl"

    )

    imputer = joblib.load(

        MODEL_PATH / "imputer.pkl"

    )

    scaler = joblib.load(

        MODEL_PATH / "scaler.pkl"

    )

    return model, imputer, scaler