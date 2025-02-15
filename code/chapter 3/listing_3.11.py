import pandas as pd
from scipy import stats
import numpy as np

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    distrib = df['Age'].dropna()

    # Using the Z-Score method on ages
    z_scores = np.abs(stats.zscore(distrib))
    outliers = distrib[z_scores > 3]
    
    print("Number of outliers", len(outliers))
    print(', '.join(map(str, outliers.values)))