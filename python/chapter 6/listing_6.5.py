import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

np.random.seed(1)
NBROWS = 5000

def plotGraph(pdf, pscaled_df):
    fig, (a, b) = plt.subplots(ncols=2, figsize=(16, 5))
    a.set_title("Before scaling")
    b.set_title("After Scaling")
    line_styles = ['-', '--', ':']  # Different line styles for the curves

    for i, col in enumerate(pdf.columns):
        sns.kdeplot(pdf[col], ax=a, linestyle=line_styles[i % len(line_styles)])
        sns.kdeplot(pscaled_df[col], ax=b, linestyle=line_styles[i % len(line_styles)])

    a.legend(pdf.columns, title="Features", loc="upper right")
    b.legend(pdf.columns, title="Features", loc="upper right")
    plt.show()

if __name__ == "__main__":
    df = pd.DataFrame({
        'A': np.random.normal(0, 2, NBROWS),
        'B': np.random.normal(5, 3, NBROWS),
        'C': np.random.normal(-5, 5, NBROWS)
    })

    scaler = MinMaxScaler()
    keepCols = ['A', 'B', 'C']
    scaled_df = scaler.fit_transform(df[keepCols])
    scaled_df = pd.DataFrame(scaled_df, columns=keepCols)

    plotGraph(df[keepCols], scaled_df)