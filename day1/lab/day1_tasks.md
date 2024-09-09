# Day 1 Lab: Introduction to MLOps

**Table of contents:**

- [Day 1 Lab: Introduction to MLOps](#day-1-lab-introduction-to-mlops)
  - [Theory Overview](#theory-overview)
    - [Repository and Version Control](#repository-and-version-control)
    - [Git and `.gitignore`](#git-and-gitignore)
    - [Python Virtual Environment and `requirements.txt`](#python-virtual-environment-and-requirementstxt)
    - [`.env` Files and Environment Variables](#env-files-and-environment-variables)
    - [Branching Strategies in Git](#branching-strategies-in-git)
    - [Introduction to Testing in ML](#introduction-to-testing-in-ml)
  - [Part 1: Repository Setup and Version Control](#part-1-repository-setup-and-version-control)
    - [Task 1: Create a New Repository](#task-1-create-a-new-repository)
    - [Task 2: Initialize Git and Set Up `.gitignore`](#task-2-initialize-git-and-set-up-gitignore)
  - [Part 2: Setting Up Python Environment](#part-2-setting-up-python-environment)
    - [Task 1: Create and Activate Python Virtual Environment](#task-1-create-and-activate-python-virtual-environment)
    - [Task 2: Create and Populate `requirements.txt`](#task-2-create-and-populate-requirementstxt)
  - [Part 3: Build a Simple ML Pipeline](#part-3-build-a-simple-ml-pipeline)
    - [Task 1: Load and Explore the Iris Dataset](#task-1-load-and-explore-the-iris-dataset)
    - [Task 2: Train a Logistic Regression Model](#task-2-train-a-logistic-regression-model)
    - [Task 3: Write and Run a Simple Unit Test](#task-3-write-and-run-a-simple-unit-test)
    - [Task 4: Visualize Data and Model Performance](#task-4-visualize-data-and-model-performance)
  - [Part 4: Collaborate Using Branches and Pull Requests](#part-4-collaborate-using-branches-and-pull-requests)
    - [Task 1: Partner Repository Review and Pull Request](#task-1-partner-repository-review-and-pull-request)
  - [`[BONUS]` Part 5: Handling Secret Files](#bonus-part-5-handling-secret-files)
    - [Task 1: Accidentally Push a Secret File and Remove It](#task-1-accidentally-push-a-secret-file-and-remove-it)
  - [Lab Wrap-Up: What We Learned](#lab-wrap-up-what-we-learned)
  - [Bonus Material](#bonus-material)
    - [Best Practices and Useful Links](#best-practices-and-useful-links)
    - [Practice Git Skills](#practice-git-skills)

## Theory Overview

### Repository and Version Control

- **Repository**: A repository (or repo) is a central place where all the files for a particular project are stored. It contains the project's code, configuration files, documentation, and version history. GitHub and GitLab are platforms that host repositories and provide version control services.
  - **Example**: You can create a repository for your MLOps project where you track changes to your code and collaborate with others.

### Git and `.gitignore`

- **Git**: Git is a distributed version control system that allows multiple people to work on a project simultaneously. It tracks changes to files and enables collaboration through branches and commits.
  - **Example**: You use Git to commit changes to your code, allowing you to keep a history of modifications and collaborate with others.
- **`.gitignore`**: This file tells Git which files or directories to ignore when committing changes. It prevents unnecessary files from being tracked.
  - **Example**: You might add `__pycache__/` to `.gitignore` to avoid tracking Python bytecode files.

### Python Virtual Environment and `requirements.txt`

- **Python Virtual Environment**: A virtual environment is an isolated environment in which you can install packages separately from the system-wide Python installation. It helps manage dependencies and avoid conflicts.
  - **Example**: By creating a virtual environment, you ensure that the libraries used in your project do not affect other Python projects.
- **`requirements.txt`**: This file lists all the Python packages required for a project. It allows others to replicate the environment easily.
  - **Example**: A `requirements.txt` file might include packages like `scikit-learn` and `pandas`, which are needed to run your ML code.

### `.env` Files and Environment Variables

- **Environment Variables**: Environment variables are used to store configuration values and secrets (like API keys or database credentials) that your application needs to run. These variables are typically stored in a `.env` file in your project directory.
  - **Example**: A `.env` file might contain a variable like `SECRET_KEY=mysecretkey123` that your application uses for security.
- **`.env` Files in Git**: It's important to ensure that `.env` files are not tracked by Git to prevent sensitive information from being exposed. This is typically managed by adding `.env` to your `.gitignore` file.
  - **Example**: Adding `.env` to `.gitignore` ensures that your environment variables are not accidentally committed to your repository.

### Branching Strategies in Git

- **Branching**: Branching allows you to create a separate line of development in your repository. It enables you to work on features or fixes without affecting the main codebase.
  - **Example**: You can create a branch named `feature/new-model` to develop a new machine learning model, keeping the main branch clean.
- **Merging**: Merging is the process of integrating changes from one branch into another. It is commonly used to bring feature changes back into the main branch after development is complete.
  - **Example**: Once you finish developing a new model on a feature branch, you can merge it into the main branch.

### Introduction to Testing in ML

- **Testing**: Testing ensures that code works as expected and helps identify bugs or issues early. In ML, testing can include checking model performance, data integrity, and code functionality.
  - **Example**: Writing a test to verify that your model achieves a minimum accuracy ensures that any changes don't degrade model performance.

## Part 1: Repository Setup and Version Control

### Task 1: Create a New Repository

- **Objective**: Introduce version control using GitHub.
- **Instructions:**
  1. Go to [GitHub](https://github.com/).
  2. Create a new repository (e.g., `mlops-course`).
  3. Clone the repository to your local machine.

### Task 2: Initialize Git and Set Up `.gitignore`

- **Objective**: Initialize Git and set up a `.gitignore` file.
- **Instructions:**
  1. Initialize Git in your project directory.
  2. Create a `.gitignore` file and add entries to ignore unnecessary files (e.g., the pycache files).
  3. Commit and push your changes to GitHub.

## Part 2: Setting Up Python Environment

### Task 1: Create and Activate Python Virtual Environment

- **Objective**: Set up a clean Python environment using `virtualenv`.
- **Instructions:**
  1. Install `virtualenv` if not already installed.
  2. Create and activate a new virtual environment.

### Task 2: Create and Populate `requirements.txt`

- **Objective**: Document project dependencies using `requirements.txt`.
- **Instructions:**
  1. Create a `requirements.txt` file in your project directory.
  2. Add the required libraries to `requirements.txt` (e.g., `numpy`).
  3. Install dependencies from `requirements.txt` and verify the installation.

## Part 3: Build a Simple ML Pipeline

**Note**: If you find it easier, you can initially write and test your code in a Jupyter Notebook (`.ipynb`). This allows for interactive coding and testing. Once you have verified your code works correctly, copy it into Python functions and create a working script (`.py`).

### Task 1: Load and Explore the Iris Dataset

- **Objective**: Load and examine a public dataset.
- **Instructions:**
  1. Create a new branch for this task.
  2. Write code to load the [Iris dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html) and print the first few rows of the DataFrame.
  3. Commit and push your changes to GitHub.

### Task 2: Train a Logistic Regression Model

- **Objective**: Build and evaluate a simple model.
- **Instructions:**
  1. Create a new branch for this task.
  2. Write code to perform a train-test split and to train a Logistic Regression model on the Iris dataset.
  3. Evaluate the model's accuracy and print the result.
  4. Commit and push your changes to GitHub.

### Task 3: Write and Run a Simple Unit Test

- **Objective**: Introduce the concept of testing in ML pipelines.
- **Instructions:**
  1. Create a new branch for this task.
  2. Write at least one unit tests for the code you have implemented.
  3. Run the tests using a testing framework like `pytest`.
  4. Commit and push your changes to GitHub.

### Task 4: Visualize Data and Model Performance

- **Objective**: Visualize data and model outputs.
- **Instructions:**
  1. Create a new branch for this task.
  2. Write code to create visualizations for the dataset (e.g., plot a histogram of a feature, or scatter plot of two features)
  3. Write code to create visualizations for the model performance (e.g., plot the confusion matrix).
  4. Commit and push your changes to GitHub.

## Part 4: Collaborate Using Branches and Pull Requests

### Task 1: Partner Repository Review and Pull Request

- **Objective**: Gain hands-on experience with branching, pull requests, and collaboration.
- **Instructions:**
  1. Pair up with a classmate and fork their repository.
  2. Clone your forked repository to your local machine.
  3. Create a new branch and add a `README.md` file to your partner's repository.
  4. Commit and push your changes.
  5. Open a pull request to merge your changes into the main branch of your partner's repository.
  6. Your partner should review the changes and ultimately merge them into the repository.

## `[BONUS]` Part 5: Handling Secret Files

### Task 1: Accidentally Push a Secret File and Remove It

- **Objective**: Learn how to handle and remove sensitive data that has been accidentally pushed to a repository.
- **Instructions:**
  1. Create a `.env` file containing a mock secret key.
  2. Add and commit the `.env` file to your repository by mistake.
  3. Remove the `.env` file from the repository.

## Lab Wrap-Up: What We Learned

- **Repository and Version Control**: We learned how to create and manage a repository using GitHub, initialize version control, and set up `.gitignore` to exclude unnecessary files.
- **Python Environment Setup**: We set up a Python virtual environment to isolate project dependencies and documented these dependencies using `requirements.txt`.
- **Building ML Pipelines**: We built a simple ML pipeline using the Iris dataset, performed data exploration, trained a logistic regression model, and added simple unit tests to ensure our model's performance.
- **Git Branching and Merging**: We explored how to create branches for new features and merge them back into the main branch.
- **Collaboration Using Pull Requests**: We practiced forking repositories, creating branches, and making pull requests. We also learned about the importance of reviewing and merging changes in a collaborative environment.
- **Handling Secrets in Git**: We learned how to handle and permanently remove sensitive data from a Git repository to ensure security.

## Bonus Material

### Best Practices and Useful Links

- **Branching Strategy**: Use branches for new features, bug fixes, or experiments. This keeps the main branch clean and stable.
  - [GitHub Flow](https://guides.github.com/introduction/flow/) is a popular branching strategy.
- **Commit Messages**: Write clear and descriptive commit messages. This helps others understand the purpose of each change.
  - [How to Write a Commit Message](https://chris.beams.io/posts/git-commit/) provides guidelines for effective commit messages.
- **Pull Request Reviews**: Always review pull requests carefully. Leave constructive feedback and ensure code quality and functionality.
- **Useful links**:
  - [Generate .gitignore files](https://www.toptal.com/developers/gitignore)
  - [How to work with multiple GitHub accounts on a single machine?](https://gist.github.com/rahularity/86da20fe3858e6b311de068201d279e3).
  - [Requirements.txt File Format](https://pip.pypa.io/en/stable/reference/requirements-file-format/)

### Practice Git Skills

- **Git Exercises and Tutorials**: Additional exercises to improve your Git skills.
  - [Git Immersion](http://gitimmersion.com/)
- **Learn Git Branching**: An interactive tool to practice Git branching and merging.
  - [Learn Git Branching](https://learngitbranching.js.org/)
