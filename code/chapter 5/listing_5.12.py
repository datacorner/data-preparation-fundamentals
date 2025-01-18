import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "/titanic/train.csv")

    features = ['Pclass', 'Age', 'Fare'] #A
    X = df[features].copy()

    imputer = SimpleImputer(strategy='mean') #B
    X = pd.DataFrame(imputer.fit_transform(X), columns=X.columns)

    scaler = StandardScaler() #C
    X_scaled = scaler.fit_transform(X)
    print(X_scaled)
