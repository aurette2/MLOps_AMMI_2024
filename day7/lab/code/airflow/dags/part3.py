import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime
import logging
import os

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 9, 19),
    'retries': 1
}

# Define the DAG
dag = DAG(
    'fetch_process_save_weather_data_with_github',
    default_args=default_args,
    description='A DAG to fetch, process, save weather data, and trigger GitHub Actions workflow',
    schedule_interval=None
)

# Fetch the GitHub token from Airflow variables
GITHUB_TOKEN = Variable.get("GITHUB_TOKEN")

# GitHub repository details
REPO = 'aurette2/MLOps_AMMI_2024'
WORKFLOW_ID = 'airflow-temperature.yml' 

# Fetch weather data task
def fetch_weather_data(ti):
    print("here1")
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/senegal?unitGroup=metric&key=DEDDS5V8SXABNH432KZVFBD9Y&contentType=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['days'][0]['temp']  # Fetching the temperature of the day
        logging.info(f"Fetched temperature: {temperature}")
        ti.xcom_push(key='temperature', value=temperature)
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")

# Convert temperature to Fahrenheit
def convert_temperature(ti):
    temperature_celsius = ti.xcom_pull(task_ids='fetch_weather_data', key='temperature')
    temperature_fahrenheit = (temperature_celsius * 9/5) + 32
    logging.info(f"Converted temperature to Fahrenheit: {temperature_fahrenheit}")
    ti.xcom_push(key='converted_temperature', value=temperature_fahrenheit)

# Task to trigger GitHub Actions workflow
def trigger_github_workflow(ti):
    temperature = ti.xcom_pull(task_ids='convert_temperature', key='converted_temperature')
    
    url = f"https://api.github.com/repos/{REPO}/actions/workflows/{WORKFLOW_ID}/dispatches"
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    data = {
        "ref": "main",
        "inputs": {
        "temperature": str(temperature) 
    }
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 204:
        logging.info(f"Successfully triggered GitHub Actions workflow with temperature: {temperature}")
    else:
        raise Exception(f"Failed to trigger GitHub workflow: {response.status_code}, {response.text}")

# Define the tasks
fetch_weather_task = PythonOperator(
    task_id='fetch_weather_data',
    python_callable=fetch_weather_data,
    dag=dag
)

convert_temperature_task = PythonOperator(
    task_id='convert_temperature',
    python_callable=convert_temperature,
    dag=dag
)

trigger_github_task = PythonOperator(
    task_id='trigger_github_workflow',
    python_callable=trigger_github_workflow,
    dag=dag
)

# Set the task sequence
fetch_weather_task >> convert_temperature_task >> trigger_github_task
