import os
import pickle
from contextlib import asynccontextmanager
from typing import Annotated

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field

load_dotenv()

ml_models = {}


class IrisData(BaseModel):
    sepal_length: float = Field(
        default=1.1, gt=0, lt=10, description="Sepal length is in range (0,10)"
    )
    sepal_width: float = Field(default=3.1, gt=0, lt=10)
    petal_length: float = Field(default=2.1, gt=0, lt=10)
    petal_width: float = Field(default=4.1, gt=0, lt=10)


def load_model(path: str):
    if not path:
        return None

    model = None
    with open(path, "rb") as f:
        model = pickle.load(f)
    return model


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["logistic_model"] = load_model(os.getenv("LOGISTIC_MODEL"))
    ml_models["rf_model"] = load_model(os.getenv("RF_MODEL"))

    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


# Create a FastAPI instance
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Hello World!"}


# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}


@app.get("/new_endpoint")
async def new_endpoint():
    return {"new": "endpoint"}


@app.get("/models")
async def list_models():
    return {"available_models": list(ml_models.keys())}


@app.post("/predict/{model_name}")
async def predict(
    model_name: Annotated[str, Path(pattern=r"^(logistic_model|rf_model)$")],
    iris_data: IrisData,
):
    input_data = [
        [
            iris_data.sepal_length,
            iris_data.sepal_width,
            iris_data.petal_length,
            iris_data.petal_width,
        ]
    ]

    if model_name not in ml_models.keys():
        raise HTTPException(status_code=404, detail="Model not found.")

    model = ml_models[model_name]
    prediction = model.predict(input_data)

    return {"model": model_name, "prediction": int(prediction[0])}
