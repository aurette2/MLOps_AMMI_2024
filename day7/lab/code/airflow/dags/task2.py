from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import logging

# Define the default arguments
default_args = {
    # 'owner': 'airflow',
    'start_date': datetime(2023, 9, 18),
    'retries': 1
}

# Define the DAG
dag = DAG(
    'task2_dag',
    default_args=default_args,
    description='A DAG with Bash and Python tasks',
    schedule_interval=None
)

# Define the Bash task
bash_task = BashOperator(
    task_id='bash_task',
    bash_command='echo "Running Bash task"',
    dag=dag
)

# Define the Python task
def hello_from_airflow():
    logging.info("Hello from Airflow")

python_task = PythonOperator(
    task_id='python_task',
    python_callable=hello_from_airflow,
    dag=dag
)

# Set the task sequence
bash_task >> python_task
