# Launch webserver
# source .venv/bin/activate
# airflow db reset -y
# airflow users create \
#     --username admin \
#     --firstname Peter \
#     --lastname Parker \
#     --role Admin \
#     --email spiderman@superhero.org

# airflow users list
export AIRFLOW_HOME=${PWD}/airflow
airflow webserver --port 8000  # http://localhost:8080