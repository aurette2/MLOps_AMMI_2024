import pandas as pd
from sklearn.datasets import load_iris

def load_and_display_iris():
    # Load the Iris dataset
    data = load_iris()
    data_df = pd.DataFrame(data=data.data, columns=data.feature_names)
    data_df['target'] = data.target

    print(data_df.head())
    return data_df

if __name__ == "__main__":
    load_and_display_iris()

