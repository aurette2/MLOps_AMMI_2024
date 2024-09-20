import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 9, 19),
    'retries': 1
}

# API details
API_KEY = 'DEDDS5V8SXABNH432KZVFBD9Y'  # Replace with your Visual Crossing API key
CITY = 'senegal'
BASE_URL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

# Fetch weather data task
def fetch_weather_data(ti):
    url = f"{BASE_URL}{CITY}?unitGroup=metric&key={API_KEY}&contentType=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        logging.info(f"loading temperature ....")
        temperature = data['days'][0]['temp'] 
        ti.xcom_push(key='temperature', value=temperature)
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    
def convert_temperature(ti):
    temperature = ti.xcom_pull(task_ids='fetch_weather_data', key='temperature')
    temperatureF = (temperature * 9/5) + 32
    ti.xcom_push(key='converted_temperature', value=temperatureF)
    logging.info(f"temperature converted")

def save_temperature_data(ti):
    temperature = ti.xcom_pull(task_ids='convert_temperature', key='converted_temperature')
    with open('./weather_data.txt', 'w') as file:
        file.write(f"The temperature in {CITY} is {temperature}°F")
    logging.info(f"Temperature data saved to file.")

# Define the DAG
dag = DAG(
    'fetch_save_weather_data',
    default_args=default_args,
    description='A DAG to fetch, process, and save weather data',
    schedule_interval=None
)

# Define the task to fetch weather data
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

save_temperature_task = PythonOperator(
    task_id='save_temperature',
    python_callable=save_temperature_data,
    dag=dag
)

fetch_weather_task >> convert_temperature_task #>> save_temperature_task
convert_temperature_task >> save_temperature_task