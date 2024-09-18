# Lab Instructions: Monitoring and Drift Detection

## Table of Contents

- [Lab Instructions: Monitoring and Drift Detection](#lab-instructions-monitoring-and-drift-detection)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Theoretical Concepts](#theoretical-concepts)
    - [Data Drift in Machine Learning Systems](#data-drift-in-machine-learning-systems)
    - [Drift Detection Tools](#drift-detection-tools)
    - [FastAPI Background Tasks](#fastapi-background-tasks)
    - [Building an Observability Pipeline](#building-an-observability-pipeline)
  - [Lab Instructions](#lab-instructions)
    - [Part 1: Drift Detection with Alibi Detect](#part-1-drift-detection-with-alibi-detect)
    - [Part 2: Monitoring and Reporting with Evidently](#part-2-monitoring-and-reporting-with-evidently)
    - [`BONUS` Part 3: Building a Monitoring Pipeline in FastAPI](#bonus-part-3-building-a-monitoring-pipeline-in-fastapi)
      - [Task 1: Create a Background Task for Logging Requests](#task-1-create-a-background-task-for-logging-requests)
      - [Task 2: Load Original and Production Data](#task-2-load-original-and-production-data)
      - [Task 3: Create a Dashboard with Evidently](#task-3-create-a-dashboard-with-evidently)
      - [Task 4: Create a Monitoring Endpoint](#task-4-create-a-monitoring-endpoint)
  - [Conclusion](#conclusion)
  - [Useful Links](#useful-links)

## Overview

In this lab, you will explore how to monitor and detect data drift in machine learning systems. Using tools like `Alibi Detect` and `Evidently`, you'll learn how to monitor data and model quality. Additionally, you will implement FastAPI background tasks to simulate logging input data and predictions. Finally, you'll schedule drift detection to run every few requests and generate monitoring reports.

## Theoretical Concepts

### Data Drift in Machine Learning Systems

**Data Drift** refers to changes in the input data that can negatively affect the performance of machine learning models over time. This is particularly important for deployed models because they are trained on historical data and may encounter unseen or shifted distributions in production.

Types of drift:

- **Feature Drift (Covariate Shift)**: Changes in the input features’ distribution.
- **Target Drift**: Changes in the distribution of the target labels.
- **Concept Drift**: Changes in the relationship between input features and the target variable.

### Drift Detection Tools

**Alibi Detect** is a popular tool used to detect different types of drift in real-time. It supports various drift detection methods, such as:

- **KS-Drift** for continuous features, which measures the difference in distributions using the Kolmogorov-Smirnov test.
- **Chi-Square Drift** for categorical features, which compares frequency distributions between two datasets.

**Evidently** is another tool designed for monitoring data and model quality in production. It generates reports and dashboards to visualize key metrics, including:

- **Data Drift**: Tracks changes in feature distributions over time.
- **Data Quality**: Checks for anomalies, missing values, and inconsistent feature types.

### FastAPI Background Tasks

**Background Tasks** in FastAPI allow you to run tasks in the background while returning responses immediately. This is useful when performing tasks that don’t need to block the main request/response cycle, such as logging, data storage, or sending alerts.

### Building an Observability Pipeline

When developing machine learning systems, it’s crucial to have monitoring pipelines that detect drift, track performance, and log system metrics. In this lab, you’ll implement a basic observability pipeline in FastAPI using background tasks, drift detection tools (Alibi Detect), and reporting tools (Evidently).

## Lab Instructions

### Part 1: Drift Detection with Alibi Detect

In this part, we will use the `alibi-detect` library to monitor data drift in the Iris dataset.

**Instructions:**

- Open the provided Jupyter Notebook (`monitoring_alibi_detect_tasks.ipynb`) and follow the tasks and comments inside.
- The notebook includes pre-filled code cells for you to work on drift detection using KS-Drift for numerical data and Chi-Square Drift for categorical data.
- You will simulate data drift and observe how the drift detection reacts to these changes.

---

### Part 2: Monitoring and Reporting with Evidently

In this part, you will learn how to use `evidently` to create dashboards and reports for monitoring the quality and distribution of data over time.

**Instructions:**

- Open the provided Jupyter Notebook (`monitoring_evidently_tasks.ipynb`) and follow the instructions and comments.
- This notebook will guide you through creating monitoring reports, running data validation checks, and visualizing changes in the data distribution with Evidently.

---

### `BONUS` Part 3: Building a Monitoring Pipeline in FastAPI

#### Task 1: Create a Background Task for Logging Requests

We will simulate logging input data and predictions to a global variable, mimicking the behavior of logging to a database.

**Instructions:**

- Create a function that logs (appends) needed feature/prediction variables to a global variable `DATA_LOG`.
- Adjust the FastAPI's endpoint `/predict` so that it calls the logging function as `BackgroundTasks`
  
#### Task 2: Load Original and Production Data

Now, we need to load two datasets the reference dataset (original iris dataset) and the production dataset (the one from logs).

**Instructions:**

- Write a function to load the Iris dataset as the reference dataset. Make sure its loaded as a pandas DataFrame.
- Write a function to load the data from global variable data_log. Make sure its loaded as a pandas DataFrame.
- Create a new global variable `WINDOW_SIZE`.
- Adjust last function so that you can load last `WINDOW_SIZE` records from the data log.

#### Task 3: Create a Dashboard with Evidently

We will now create a function that compares the original dataset with the production data (last `WINDOW_SIZE` requests) and generates a drift detection report.

**Instructions:**

- Use Evidently to build a preset dashboard that compares the reference and production datasets (make sure to load the data with functions from part 2).
- This dashboard should include drift detection reports like DataDriftPreset and DataQualityPreset.

#### Task 4: Create a Monitoring Endpoint

Finally, create an endpoint `/monitoring` that triggers the drift detection report and returns an HTML report showing the comparison between the original and production datasets.

**Instructions:**

- Write a `/monitoring` endpoint that generates the Evidently report.
- Serve the report as an HTML file.

## Conclusion

In this lab, you built a foundational observability pipeline for machine learning systems. You learned how to:

- Detect data drift using Alibi Detect (KS-Drift and Chi-Square Drift).
- Create detailed data drift and data quality reports using Evidently.
- Use FastAPI background tasks to simulate logging production data.
- Perform periodic drift detection and monitor system health via an API.

These tools and techniques form the basis of robust model monitoring, ensuring your deployed models perform well over time by responding to changes in input data.

## Useful Links

- [Alibi Detect Documentation](https://docs.seldon.io/projects/alibi-detect/en/stable/)
- [Alibi Detect Tutorial](https://medium.com/@sharangp/the-perfect-alibi-catching-data-drift-with-alibi-detect-eebbf527ef78)
- [Evidently Documentation](https://docs.evidentlyai.com/)
- [Evidently Statistical Tests](https://docs.evidentlyai.com/user-guide/customization/options-for-statistical-tests)
- [FastAPI Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)
- [Monitoring ML Models with Evidently and FastAPI](https://duarteocarmo.com/blog/monitoring-ml-models-fastapi-evidently)
