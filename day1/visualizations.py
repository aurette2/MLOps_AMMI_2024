
import matplotlib.pyplot as plt
import seaborn as sns
# from sklearn.datasets import load_iris
# from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# from loadData import load_and_display_iris
# from train import split, fit, predict


def visualize_dataset(data_df):
    # Plot histogram of the first feature (sepal length)
    plt.figure(figsize=(8, 6))
    sns.histplot(data_df['sepal length (cm)'], kde=True)
    plt.title('Distribution of Sepal Length')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Frequency')
    plt.show()

    # Plot a scatter plot between two features (sepal length and sepal width)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=data_df['sepal length (cm)'], y=data_df['sepal width (cm)'], hue=data_df['target'])
    plt.title('Sepal Length vs Sepal Width')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.legend(title='Target')
    plt.show()


def visualize_model_performance(y_test, y_pred):
    # Plot confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.show()

# if __name__ == "__main__":
#     data = load_iris()
#     data_df = load_and_display_iris(data)
#     visualize_dataset(data_df)

#     X_train, X_test, y_train, y_test= split(data_df)
#     model = LogisticRegression(max_iter=200)
#     fit(model, X_train, y_train)
#     y_pred = predict(model, X_test)
#     visualize_model_performance(y_test, y_pred)
