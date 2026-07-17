from fastapi import FastAPI

from src.api.routes import router


app = FastAPI(

    title="Enterprise AI-Powered Credit Risk Intelligence Platform",

    description="Loan Default Prediction API using LightGBM",

    version="1.0.0"

)


app.include_router(

    router

)


@app.get("/")

def home():

    return {

        "message": "Welcome to Enterprise AI-Powered Credit Risk Intelligence Platform",

        "docs": "/docs",

        "health": "/health"

    }