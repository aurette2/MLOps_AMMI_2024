from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from loadData import load_and_display_iris

#Split data into train and test sets
def split(data_df):
    X = data_df.drop('target', axis=1)
    y = data_df['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Initialize and train the Logistic Regression model
def fit(model, X_train, y_train):
    model.fit(X_train, y_train)

# Make predictions on the test set
def predict(model, X_test):
    y_pred = model.predict(X_test)
    return y_pred

    

if __name__ == "__main__":
    # get data from load file
    data_df = load_and_display_iris()

    #Splitting the dataset
    X_train, X_test, y_train, y_test = split(data_df)

    #Initialisation, training and evaluating the model
    model = LogisticRegression(max_iter=200)
    fit(model, X_train, y_train)
    y_pred = predict(model, X_test)

    # Evaluate the model's accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy of the Logistic Regression model: {accuracy:.2f}")