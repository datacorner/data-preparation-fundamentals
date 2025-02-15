import pandas as pd
import matplotlib.pyplot as plt

def iqr_method(data):
    """ This function identifies potential outliers in a dataset using the 
        Interquartile Range (IQR) method. It calculates the IQR, determines the 
        lower and upper bounds for outlier detection, and returns data points 
        that fall outside these bounds.
    Parameters:
        data (pd.Series): A Pandas Series containing numerical data to analyze for outliers.
    Returns:
        pd.Series: A subset of the input Series containing the detected outliers.
    """
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    print(f"IQR={IQR}")
    lower_bound = Q1 - 1.5 * IQR
    print(f"lower_bound={lower_bound}")
    upper_bound = Q3 + 1.5 * IQR
    print(f"upper_bound={upper_bound}")
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    return outliers

if __name__ == "__main__":
    df = pd.read_csv("../data/titanic/train.csv")
    distrib = df['Age'].dropna()
    
    # Create the box plot to visualize the Age repartition
    plt.figure(figsize=(10, 6))
    distrib.plot(kind='box')
    plt.title('Age Distribution in the Dataset')
    plt.ylabel('Age distribution')
    plt.xlabel('Age')
    plt.grid(True, axis='y', linestyle='--', alpha=0.7) # Add grid for better readability
    # Show the plot
    plt.show()
    
    # IQR method
    iqr_outliers = iqr_method(distrib)
    print("Number of outliers", len(iqr_outliers))
    print(', '.join(map(str, iqr_outliers.values)))