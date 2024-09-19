from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
# import logging

# Define the default arguments
default_args = {
    # 'owner': 'airflow',
    'start_date': datetime(2023, 9, 18),
    'retries': 1
}

# Define the Python functions for the tasks
def print_starting_dag():
    # logging.info("Starting Airflow DAG")
    print(f'Starting Airflow DAG')

def print_current_time():
    # logging.info(f"Current date and time: {datetime.now()}")
    print(f'Current date and time: {datetime.now()}')


# Define the DAG
with DAG(
    'task1_dag',
    default_args=default_args,
    description='Creating a Simple Airflow DAG with two Python tasks',
    schedule_interval='@daily',
    catchup=False
) as dag: 
    # Define the tasks
    task_1 = PythonOperator(
        task_id='start_dag',
        python_callable=print_starting_dag,
        # dag=dag
    )

    task_2 = PythonOperator(
        task_id='print_time',
        python_callable=print_current_time,
        # dag=dag
    )

    # Set the task sequence
    task_1 >> task_2
