from fastapi import FastAPI, HTTPException
import joblib
import os
import asyncio
from dotenv import load_dotenv
from contextlib import asynccontextmanager
import numpy as np
from typing import List
from pydantic import BaseModel, Field, confloat

# Load environment variables from .env file
load_dotenv()

models = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load models from the paths defined in .env file
    logistic_model_path = os.getenv('LOGISTIC_MODEL')
    rf_model_path = os.getenv('RF_MODEL')

    models['logistic'] = joblib.load(logistic_model_path)
    models['random_forest'] = joblib.load(rf_model_path)

    yield
    models.clear()


class IrisFeatures(BaseModel):
    sepal_length: confloat(gt=0, le=10.0) = Field(..., description="Sepal length in cm (0 < value ≤ 10)")
    sepal_width: confloat(gt=0, le=5.0) = Field(..., description="Sepal width in cm (0 < value ≤ 5)")
    petal_length: confloat(gt=0, le=7.0) = Field(..., description="Petal length in cm (0 < value ≤ 7)")
    petal_width: confloat(gt=0, le=3.0) = Field(..., description="Petal width in cm (0 < value ≤ 3)")

    class Config:
        schema_extra = {
            "example": {
                "sepal_length": 5.1,
                "sepal_width": 3.5,
                "petal_length": 1.4,
                "petal_width": 0.2
            }
        }


app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "Hello world"}

@app.get("/health")
def health_check():
    return {"status": "running"}

@app.get("/models")
def list_models():
    return {"List of models": list(models.keys())}

@app.post("/predict/{model_name}")
# async def predict(model_name: str, features: List[float]):
async def predict(model_name: str, features: IrisFeatures):
    await asyncio.sleep(2) 
    if model_name not in models:
        raise HTTPException(status_code=404, detail="Model not found")
    
    # # Check if the input data has exactly 4 features
    # if len(features.values()) != 4:
    #     raise HTTPException(status_code=400, detail="Input data must contain exactly 4 features.")

    # Get the selected model
    model = models[model_name]

    input_data = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])

    
    # Make the prediction
    prediction = model.predict(input_data).tolist()
    
    return {"model": model_name, "prediction": prediction}