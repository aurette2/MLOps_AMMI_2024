from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define the default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 9, 18),
    'retries': 1
}

# Define the DAG and set schedule_interval to every 5 minutes
dag = DAG(
    'simple_dag_every_5_minutes',
    default_args=default_args,
    description='A simple DAG running every 5 minutes',
    schedule_interval='*/5 * * * *'  # Every 5 minutes
)

# Define the Python functions for the tasks
def print_starting_dag():
    print("Starting Airflow DAG")

def print_current_time():
    print(f"Current date and time: {datetime.now()}")

# Define the tasks
task_1 = PythonOperator(
    task_id='start_dag',
    python_callable=print_starting_dag,
    dag=dag
)

task_2 = PythonOperator(
    task_id='print_time',
    python_callable=print_current_time,
    dag=dag
)

# Set the task sequence
task_1 >> task_2
