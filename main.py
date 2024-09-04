from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


from loadData import load_and_display_iris
from train import split, fit, predict
from visualizations import visualize_dataset, visualize_model_performance


data = load_iris()
data_df = load_and_display_iris(data)
visualize_dataset(data_df)
X_train, X_test, y_train, y_test= split(data_df)
model = LogisticRegression(max_iter=200)
fit(model, X_train, y_train)
y_pred = predict(model, X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the Logistic Regression model: {accuracy:.2f}")
visualize_model_performance(y_test, y_pred)