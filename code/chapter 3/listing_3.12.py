import pandas as pd
from scipy import stats

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    distrib = df['Age'].dropna()

    # Using the Shapiro-Wilk test on ages
    statistic, p_value = stats.shapiro(distrib)
    print(f"Shapiro-Wilk test results:")
    print(f"Statistic: {statistic:.6f}")
    print(f"p-value: {p_value:.6f}")
    if p_value > 0.05:
        print("The age distribution is likely normal (fail to reject H0)")
    else:
        print("The age distribution is likely not normal (reject H0)")
