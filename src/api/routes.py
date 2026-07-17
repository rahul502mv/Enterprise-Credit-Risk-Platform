import pandas as pd

from fastapi import APIRouter

from src.api.schemas import PredictionRequest, PredictionResponse

from src.models.predict import predict_customer


router = APIRouter()


def risk_category(probability):

    if probability < 0.20:

        return "Low Risk"

    elif probability < 0.50:

        return "Medium Risk"

    else:

        return "High Risk"


def recommendation(risk):

    if risk == "Low Risk":

        return "Approve Loan"

    elif risk == "Medium Risk":

        return "Manual Review"

    else:

        return "Reject / Investigate"


@router.get("/health")

def health():

    return {

        "status": "API Running Successfully"

    }


@router.post(

    "/predict",

    response_model=PredictionResponse

)

def predict(request: PredictionRequest):

    input_df = pd.DataFrame(

        [request.features]

    )

    prediction, probability = predict_customer(

        input_df

    )

    probability = float(

        probability[0]

    )

    prediction = int(

        prediction[0]

    )

    risk = risk_category(

        probability

    )

    advice = recommendation(

        risk

    )

    return PredictionResponse(

        prediction=prediction,

        probability=probability,

        risk_category=risk,

        recommendation=advice

    )