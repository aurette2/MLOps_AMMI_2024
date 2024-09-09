# Day 2 Lab: Machine Learning Lifecycle Management

**Table of contents:**

- [Day 2 Lab: Machine Learning Lifecycle Management](#day-2-lab-machine-learning-lifecycle-management)
  - [Theory Overview](#theory-overview)
    - [ML Model Development and Lifecycle](#ml-model-development-and-lifecycle)
    - [Experiment Tracking and Management](#experiment-tracking-and-management)
    - [Version Control for Data and Models](#version-control-for-data-and-models)
    - [Tools and Frameworks for ML Lifecycle Management](#tools-and-frameworks-for-ml-lifecycle-management)
  - [Part 1: Version Control Data and Models with DVC](#part-1-version-control-data-and-models-with-dvc)
    - [Task 1: Initialize DVC and Track Data](#task-1-initialize-dvc-and-track-data)
    - [`[BONUS]` Task 2: Storing DVC Data Remotely](#bonus-task-2-storing-dvc-data-remotely)
    - [Task 3: Make Local Changes to the Dataset](#task-3-make-local-changes-to-the-dataset)
  - [Part 2: Integrating DVC with Cloud Storage](#part-2-integrating-dvc-with-cloud-storage)
    - [Task 1: Integrate DVC with Cloud Storage](#task-1-integrate-dvc-with-cloud-storage)
      - [Using Azure Blob Storage with DVC](#using-azure-blob-storage-with-dvc)
      - [Using Google Cloud Storage (GCS) with DVC](#using-google-cloud-storage-gcs-with-dvc)
      - [Using AWS S3 with DVC](#using-aws-s3-with-dvc)
  - [Part 3: Set Up Experiment Tracking with MLflow](#part-3-set-up-experiment-tracking-with-mlflow)
    - [Task 1: Install and Set Up MLflow](#task-1-install-and-set-up-mlflow)
    - [`[BONUS]` Task 2: Log Experiments Using MLflow](#bonus-task-2-log-experiments-using-mlflow)
      - [Autologging](#autologging)
      - [Manual Logging](#manual-logging)
  - [Part 4: Integrate MLflow with Azure ML](#part-4-integrate-mlflow-with-azure-ml)
    - [Task 1: Log Experiments in Azure](#task-1-log-experiments-in-azure)
    - [Task 2: Deploy an MLflow Model to Azure ML](#task-2-deploy-an-mlflow-model-to-azure-ml)
  - [Lab Wrap-Up: What We Learned](#lab-wrap-up-what-we-learned)
  - [Bonus Material](#bonus-material)
    - [Best Practices and Useful Links](#best-practices-and-useful-links)

## Theory Overview

### ML Model Development and Lifecycle

- **ML Model Development**: The process involves several stages from data collection, preprocessing, model training, evaluation, deployment, and monitoring.
  - **Lifecycle Management**: Managing the lifecycle ensures that models are reproducible, scalable, and maintainable.

### Experiment Tracking and Management

- **Experiment Tracking**: The process of logging experiments, including hyperparameters, metrics, and artifacts, to facilitate analysis and comparison.
  - **Tools**: MLflow, Weights & Biases, TensorBoard.

### Version Control for Data and Models

- **Version Control for Data**: Tracking changes to datasets over time using tools like DVC.
- **Version Control for Models**: Managing different versions of models to maintain a history of changes and facilitate rollback if necessary.

### Tools and Frameworks for ML Lifecycle Management

- **MLflow**: An open-source platform for managing the ML lifecycle, including experimentation, reproducibility, and deployment.
- **DVC**: Data Version Control (DVC) is a tool for managing datasets and model versions with Git-like functionality.

## Part 1: Version Control Data and Models with DVC

### Task 1: Initialize DVC and Track Data

- **Objective**: Learn how to use DVC to version control datasets.
- **Instructions**:
  1. Install DVC:

  2. Initialize DVC in your Git repository (make sure to position yourself in the root folder) and commit the changes:

  3. Start tracking a local dataset with DVC (add it to DVC + push changes to git):

- **Explore**: Look into the metafile created for you local dataset. It contains a md5 hash value that is used for referencing the file. If you check the cache inside the `.dvc` directory you can see the file there with the name of the hash value. On GitHub only the metafile is stored/tracked.

### `[BONUS]` Task 2: Storing DVC Data Remotely

- **Objective**: Understand how to store and retrieve data using DVC remote storage.
- **Instructions:**
  1. Create a "local remote" folder (i.e., a directory in the local file system) to serve as storage. Make sure it is ignored by `.gitignore` if created/placed inside the git repo.
  
  2. Push the data to the "local remote":

  3. Test the storage. Delete the data from your initial data folder and `.dvc` cache, then pull it from 'remote':

  4. Check that the data was correctly pulled from the local folder that serves as storage.

### Task 3: Make Local Changes to the Dataset

- **Objective**: Learn how to manage dataset versions with DVC after making changes.
- **Instructions:**

  1. Make some changes to the local data (e.g., duplicate/remove a row).

  2. Track the latest version:

  3. Push the changes to the remote and commit the new metafile to git:

## Part 2: Integrating DVC with Cloud Storage

### Task 1: Integrate DVC with Cloud Storage

**Objective**: Learn how to set up and use DVC with different cloud storage providers (AWS S3, Azure Blob Storage, and Google Cloud Storage).

**Note**: Focus on a single Cloud Provider, and then proceed with other tasks. Come back to the other if you get the time.

#### Using Azure Blob Storage with DVC

1. **Set Up Azure Blob Storage**:
   - Create a storage account and container in Azure Blob Storage.

2. **Configure DVC to Use Azure Blob Storage**:
   - Install Azure CLI if not already installed and log in:

   - Configure DVC to use Azure Blob Storage:

3. **Push and Pull Data**:
   - Push data to Azure Blob Storage:

   - Pull data from Azure Blob Storage:

#### Using Google Cloud Storage (GCS) with DVC

1. **Set Up Google Cloud Storage**:
   - Create a Google Cloud project and storage bucket.

2. **Configure DVC to Use GCS**:
   - Install Google Cloud SDK and authenticate:

   - Configure DVC to use GCS:

3. **Push and Pull Data**:
   - Push data to Google Cloud Storage:

   - Pull data from Google Cloud Storage:

#### Using AWS S3 with DVC

1. **Set Up AWS S3 Bucket**:
   - Create an S3 bucket in your AWS account to store datasets and models.

2. **Configure DVC to Use S3**:
   - Install AWS CLI and configure your AWS credentials if not already done:

   - Add an S3 remote storage in your DVC project:

3. **Push and Pull Data**:
   - Push data to AWS:

   - Pull data from AWS:

## Part 3: Set Up Experiment Tracking with MLflow

### Task 1: Install and Set Up MLflow

**Objective**: Set up MLflow for logging experiments and tracking model performance.

**Instructions:**

  1. Install MLflow:

  2. Set up an MLflow tracking server:

### `[BONUS]` Task 2: Log Experiments Using MLflow

**Objective**: Learn how to log experiments, including parameters, metrics, and artifacts.

**Instructions:**

#### Autologging

  1. Open the  `mlflow_autologging.py` script.
  
  2. Modify the script to use MLflow's autologging.
  
  3. Run your script and then navigate to the MLflow UI to visualize the logged experiments and compare different runs.

#### Manual Logging

  1. Open the `iris_pipeline.py` script.

  2. Modify the script to log experiments with MLflow.

  3. Run your script and then navigate to the MLflow UI to visualize the logged experiments and compare different runs.

## Part 4: Integrate MLflow with Azure ML

### Task 1: Log Experiments in Azure

**Objective**: Configure MLflow to log experiments to Azure ML.

**Instructions**:

  1. **Set Up Azure ML Workspace**:

  2. **Configure MLflow to Use Azure ML**:
     - Use the `iris_pipeline.py` script as starter point.

### Task 2: Deploy an MLflow Model to Azure ML

**Objective**: Deploy a trained MLflow model to Azure Machine Learning.

**Instructions**:

   1. **Register a new model in Azure ML**:

## Lab Wrap-Up: What We Learned

- **Experiment Tracking**: Learned how to use MLflow to log experiments, track parameters, metrics, and artifacts, and visualize results.
- **Data and Model Version Control**: Gained hands-on experience with DVC for version-controlling data and models, ensuring traceability and reproducibility.
- **Cloud Integration**: Learned to use cloud storage and cloud-based experiment tracking tools to manage datasets, models, and experiment logs in a scalable manner.
- **Azure ML Integration**: Implemented logging and deployment of models using Azure ML to enhance reproducibility and manageability.

## Bonus Material

### Best Practices and Useful Links

- **Experiment Tracking**: Always log your experiments with sufficient detail to ensure reproducibility and ease of comparison.
- **Model Checkpointing**: Save model checkpoints regularly during training to prevent data loss and facilitate model reuse.
- **Useful links**:
  - [MLflow Documentation](https://www.mlflow.org/docs/latest/index.html)
  - [MLflow Compare runs, choose model, deploy to REST API](https://www.mlflow.org/docs/latest/getting-started/quickstart-2/)
  - [DVC Documentation](https://dvc.org/doc)
  - [Setting up MLflow on GCP](https://dlabs.ai/blog/a-step-by-step-guide-to-setting-up-mlflow-on-the-google-cloud-platform/)
  - [Setting up MLflow on AWS](https://medium.com/ama-tech-blog/mlflow-on-aws-a-step-by-step-setup-guide-8601414dd6ea)
