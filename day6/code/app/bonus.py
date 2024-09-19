from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse
from sklearn.datasets import load_iris
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, DataQualityPreset
import pandas as pd
import os

app = FastAPI()

# store logged data
DATA_LOG = []
WINDOW_SIZE = 100

# Function to log data (append input features and prediction to the global variable)
def log_data(input_data: dict, prediction: float):
    DATA_LOG.append({**input_data, 'prediction': prediction})

# Function to load the Iris dataset as a reference dataset
def load_reference_data():
    iris = load_iris(as_frame=True)
    reference_data = iris.frame
    return reference_data

# Function to load the last WINDOW_SIZE records from DATA_LOG
def load_production_data():
    if len(DATA_LOG) == 0:
        return pd.DataFrame() 
    production_data = pd.DataFrame(DATA_LOG)
    return production_data.tail(WINDOW_SIZE)

# Function to generate the Evidently dashboard comparing the reference and production datasets
def generate_evidently_report():
    reference_data = load_reference_data()
    production_data = load_production_data()
    report = Report(metrics=[DataDriftPreset(), DataQualityPreset()])
    report.run(reference_data=reference_data, current_data=production_data)
    report.save_html('evidently_report.html')

# Prediction endpoint
@app.post("/predict")
async def predict(input_data: dict, background_tasks: BackgroundTasks):
    # Extract features from input_data
    sepal_length = input_data['sepal_length']
    sepal_width = input_data['sepal_width']
    petal_length = input_data['petal_length']
    petal_width = input_data['petal_width']
    
    prediction = (sepal_length * 0.3) + (sepal_width * 0.2) + (petal_length * 0.4) + (petal_width * 0.1)
    background_tasks.add_task(log_data, input_data, prediction)
    return {"prediction": prediction}


# Monitoring endpoint to display the drift report
@app.get("/monitoring")
async def monitoring():
    generate_evidently_report()
    if os.path.exists('evidently_report.html'):
        with open('evidently_report.html', 'r') as f:
            html_content = f.read()
        return HTMLResponse(content=html_content, status_code=200)
    else:
        return {"message": "Report generation failed."}
