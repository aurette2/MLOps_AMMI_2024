import mlflow
from mlflow.models import infer_signature
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def load_dataset():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test


def train_and_log_model(params):
    X_train, X_test, y_train, y_test = load_dataset()

    model = LogisticRegression(**params)

    model.fit(X_train, y_train)
    # Predict on the test set
    accuracy = inference(model, X_test, y_test)

    # TODO: Log the hyperparameters
    mlflow.log_params(params)

    # TODO: Log the loss metric
    mlflow.log_metric("accuracy", accuracy)

    # TODO: Set a tag that we can use to remind ourselves what this run was for
    mlflow.set_tag("Training Info", "Basic LR model for iris data")

    # TODO: Infer the model signature to be used when saving model
    signature = infer_signature(X_train, model.predict(X_train))

    # TODO: Save the model, make sure to provide the signature and an input example.
    model = mlflow.sklearn.log_model(
        sk_model=model,
        artifact_path="iris_model",
        signature=signature,
        input_example=X_train,
        registered_model_name="tracking-quickstart",
    )

    return model


def inference(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Accuracy of the model is: {accuracy}.")

    return accuracy


if __name__ == "__main__":
    # TODO: Set up MLflow.
    mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")

    # Create a new MLflow Experiment
    mlflow.set_experiment("MLflow Quickstart")

    # Define the model hyperparameters
    params = {
        "solver": "lbfgs",
        "max_iter": 1000,
        "multi_class": "auto",
        "random_state": 8888,
    }
    model = train_and_log_model(params)

    X_train, X_test, y_train, y_test = load_dataset()

    # TODO: Load the model back from MLflow for more predictions
    model = mlflow.pyfunc.load_model(model.model_uri)

    accuracy = inference(model, X_test, y_test)
