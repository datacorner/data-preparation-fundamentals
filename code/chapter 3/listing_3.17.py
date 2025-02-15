import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

def compare_dist(distrib1, distrib2, nbbins = 40):
    """
    Compares and visualizes the differences between two age distributions.  
    Creates a side-by-side bar chart to highlight discrepancies in frequency across age bins.
    Parameters:
        distrib1 (pd.Series or np.ndarray): The first age distribution to compare.
        distrib2 (pd.Series or np.ndarray): The second age distribution to compare with.
        nbbins (int, optional): Number of bins for the histogram. Defaults to 40.
    """
    # Set up the plot
    plt.figure(figsize=(15, 6))
    # Define the bins
    bins = np.linspace(0, max(distrib.max(), distrib2.max()), nbbins+1)  # x bins, ranging from 0 to the max
    bin_width = bins[1] - bins[0]
    # Calculate the histograms
    hist1, _ = np.histogram(distrib1, bins=bins)
    hist2, _ = np.histogram(distrib2, bins=bins)
    # Set up the bar positions
    bar_positions = np.arange(len(bins) - 1)
    bar_width = 0.35
    # Create the side-by-side bar chart
    plt.bar(bar_positions - bar_width/2, hist1, bar_width, alpha=0.8, color='black', label='Original dataset')
    plt.bar(bar_positions + bar_width/2, hist2, bar_width, alpha=0.8, color='grey', label='Dataset updated')
    # Customize & show the plot
    plt.title('Age Distribution Comparison in dataset')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.legend()
    plt.xticks(bar_positions, [f'{int(bins[i])}-{int(bins[i+1])}' for i in range(len(bins)-1)])
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

def normalize_age(age):
    """
    Normalizes age data using the Box-Cox transformation to stabilize variance and make the data more normally distributed.  
    The transformation applies a parameter (lambda) to the age data, and the normalized data is returned.
    Parameters:
        age (pd.Series): The age data to normalize
    Returns:
        pd.Series: The normalized age data after applying the Box-Cox transformation.
    """
    age_transformed, lambda_param = stats.boxcox(age) 
    age_normalized = pd.Series(age_transformed, 
                                index=age.index, 
                                name='Age') 
    print(f"Box-Cox applied with lambda = {lambda_param:.4f}")
    return age_normalized

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    distrib = df['Age'].dropna()
    dfo = normalize_age(distrib.copy())
    compare_dist(distrib, dfo)

