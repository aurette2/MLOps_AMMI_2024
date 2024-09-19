from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
import logging

# Define default arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 9, 18),
    'retries': 1
}

# Define the DAG
dag = DAG(
    'xcom_dag',
    default_args=default_args,
    description='A DAG demonstrating XCom usage',
    schedule_interval=None 
)

# Python task to push timestamp to XCom
def push_timestamp(ti):
    current_time = datetime.now()
    ti.xcom_push(key='timestamp', value=str(current_time))
    logging.info(f"Pushed timestamp: {current_time}")

push_task = PythonOperator(
    task_id='push_timestamp',
    python_callable=push_timestamp,
    dag=dag
)

# Bash task to pull timestamp from XCom and echo it
bash_pull_task = BashOperator(
    task_id='bash_pull_timestamp',
    bash_command='echo "Pulled timestamp: {{ ti.xcom_pull(task_ids=\'push_timestamp\', key=\'timestamp\') }}"',
    dag=dag
)

# Set the task sequence
push_task >> bash_pull_task