
# Lab: Orchestration with Airflow and GitHub Actions (Student Version)

## Table of Contents

- [Lab: Orchestration with Airflow and GitHub Actions (Student Version)](#lab-orchestration-with-airflow-and-github-actions-student-version)
  - [Table of Contents](#table-of-contents)
  - [Theory Overview](#theory-overview)
    - [Orchestration in Machine Learning Pipelines](#orchestration-in-machine-learning-pipelines)
    - [Key Concepts](#key-concepts)
  - [Part 0: Setup Airflow](#part-0-setup-airflow)
  - [Part 1: Introduction to Airflow](#part-1-introduction-to-airflow)
    - [Task 1: Create a Simple Airflow DAG](#task-1-create-a-simple-airflow-dag)
    - [Task 2: Using Airflow Operators](#task-2-using-airflow-operators)
    - [Task 3: Running a DAG every 5 minutes](#task-3-running-a-dag-every-5-minutes)
    - [Task 4: Using XCom for Task Communication](#task-4-using-xcom-for-task-communication)
      - [What is `ti` in Airflow?](#what-is-ti-in-airflow)
  - [Part 2: Fetch, Process, Save](#part-2-fetch-process-save)
  - [`BONUS` Part 3: GitHub Workflow Integration](#bonus-part-3-github-workflow-integration)
    - [Task 1: GitHub Actions Workflow](#task-1-github-actions-workflow)
    - [Task 2: Generate GitHub Token with Write Permission](#task-2-generate-github-token-with-write-permission)
    - [Task 3: Airflow Task to Trigger GitHub Workflow](#task-3-airflow-task-to-trigger-github-workflow)
  - [Conclusion](#conclusion)
  - [Useful Links](#useful-links)

---

## Theory Overview

### Orchestration in Machine Learning Pipelines

Orchestration is the process of automating the execution of tasks in a pipeline. In machine learning, this often involves scheduling tasks like data fetching, data preprocessing, model training, evaluation, and deployment. Orchestration tools like **Apache Airflow** make it easier to manage complex workflows, ensuring that each step runs smoothly and at the correct time.

**Airflow** uses DAGs (Directed Acyclic Graphs) to represent workflows. Each node in the graph is a task, and the edges between them define dependencies.

### Key Concepts

- **DAG**: A Directed Acyclic Graph, which represents the entire workflow or pipeline.
- **Task**: A single step in the pipeline. Tasks can perform actions like fetching data, running scripts, or sending notifications.
- **Operator**: Defines what type of task is being performed (e.g., a Python function, a bash command, etc.).
- **GitHub Actions**: A CI/CD automation tool integrated with GitHub. It is event-driven and can be triggered by events such as code pushes, pull requests, or even API calls. It allows workflows to run custom scripts or pre-built actions.

---

## Part 0: Setup Airflow

- Use the `install.sh` script to install Airflow 2.3.3
- Make sure to export `AIRFLOW_HOME` in the terminal/command line you use. `export AIRFLOW_HOME=${PWD}/airflow`
- Inside the newly created `airflow.cfg` set `load_examples=False` and run `airflow db reset -y`
- Create a user with `Admin` role.
- Run the webserver and scheduler.
- Check that you have a working UI at localhost and sign in with the `Admin` credentials you created in previous steps.

**Note:** All DAGs you build will go into the `/dags` folder in `airflow` directory.

## Part 1: Introduction to Airflow

### Task 1: Create a Simple Airflow DAG

- Define a DAG in Airflow that runs two Python tasks in sequence.
- One task should print "Starting Airflow DAG".
- The second task should print the current date and time.

### Task 2: Using Airflow Operators

- Create a new DAG that has:
  - A Bash task that echoes "Running Bash task".
  - A Python task that prints "Hello from Airflow".
  
### Task 3: Running a DAG every 5 minutes

- Modify the DAG to run every 5 minutes using a cron expression.

**Note:** You can use [crontab.guru](https://crontab.guru/) to quickly figure out a cron schedule expression you might need.

### Task 4: Using XCom for Task Communication

In this task, you'll learn how to use XCom (Cross-Communication) to pass data between tasks. We will use both a `PythonOperator` and a `BashOperator`:

- Create a Python task that pushes the current timestamp to XCom.
- Create a Bash task that pulls the value from XCom and echoes it.

#### What is `ti` in Airflow?

In Airflow, `ti` stands for **TaskInstance**. It is an object that represents a single run of a task. When using `XCom`, we often refer to `ti` because it allows us to **push** and **pull** values (such as variables) between tasks. For example, you can push a value using `ti.xcom_push()` and retrieve it in another task with `ti.xcom_pull()`.

---

## Part 2: Fetch, Process, Save

In this part, you'll fetch weather data from an API, process it, save it to a local file.

1. **Fetch Weather Data**:
   - Create an account on [Visual Crossing](https://www.visualcrossing.com/) and get your API key.
   - Create an Airflow task that fetches weather data for a specific city (e.g., London) using the Visual Crossing API.
   - Save the fetched temperature data into XCom.

2. **Process Data**:
   - Create a new task that pulls the temperature data from XCom and converts it to any other temperature unit (i.e., Kelvin, Fahrenheit).
   - Save the converted temperature back into XCom.

3. **Save Data to File or Cloud**:
   - Add a task that saves the processed temperature data to a local file or uploads it to Google Cloud Storage.

---

## `BONUS` Part 3: GitHub Workflow Integration

In this part, you'll write a simple GitHub Actions workflow and trigger it from Airflow.

### Task 1: GitHub Actions Workflow

- Create a simple GitHub Actions workflow that echoes the temperature data passed from Airflow.
- You will need to set up the workflow dispatch with an input that accepts the temperature.

### Task 2: Generate GitHub Token with Write Permission

- Generate a GitHub token with **write access** to your repository's GitHub Actions.

### Task 3: Airflow Task to Trigger GitHub Workflow

- Add a task in your Airflow DAG that triggers the GitHub Actions workflow, passing in the temperature as an input.

---

## Conclusion

- This lab has walked you through creating and orchestrating workflows using Apache Airflow, integrating with GitHub Actions, and scaling with Google Cloud.
- These concepts will help you understand how to manage, automate, and scale workflows in real-world machine learning pipelines.

---

## Useful Links

- [Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [VisualCrossing API](https://www.visualcrossing.com/weather-api)
- [Crontab Guru](https://crontab.guru/)
