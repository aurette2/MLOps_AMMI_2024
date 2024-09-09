from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression

from day1.loadData import load_and_display_iris
from day1.train import split, predict, fit

# Check if the sizes of the train and test sets are correct
def test_train_test_split_shape():
    assert len(X_test) == 30, f"Expected 30 samples in the test set, but got {len(X_test)}"
    assert len(X_train) == 120, f"Expected 120 samples in the train set, but got {len(X_train)}"

# Check if all predicted values is in the correct range
def test_prediction_range(model):
    fit(model, X_train, y_train)
    y_pred = predict(model, X_test)
    assert set(y_pred).issubset({0, 1, 2}), f"Predictions contain unexpected values: {set(y_pred)}"


def test_accurancy(model):
    fit(model, X_train, y_train)
    y_pred = predict(model, X_test)
    accuracy = accuracy_score(y_test, y_pred)
    assert accuracy > 0.8, f"Expected accuracy > 0.8, but got {accuracy}"


def test():
    pass


if __name__ == "__main__":
    data = load_iris()
    data_df = load_and_display_iris(data)
    X_train, X_test, y_train, y_test= split(data_df)
    model = LogisticRegression(max_iter=200)
    test_train_test_split_shape()
    test_prediction_range(model)
    test_accurancy(model)