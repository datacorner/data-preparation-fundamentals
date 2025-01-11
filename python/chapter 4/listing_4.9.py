import pandas as pd
from sklearn.utils import resample

if __name__ == "__main__":
    # Sample dataset
    data = {
        'Feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Feature2': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'Class': ['Man', 'Man', 'Woman', 'Woman', 
                'Man', 'Woman', 'Woman', 'Man', 
                'Man', 'Woman']
    }
    df = pd.DataFrame(data)
    
    stratum_Man = df[df['Class'] == 'Man']
    stratum_Woman = df[df['Class'] == 'Woman']
    sample_M = resample(stratum_Man, replace=False, n_samples=int(0.5 * len(stratum_Man)))
    sample_W = resample(stratum_Woman, replace=False, n_samples=int(0.5 * len(stratum_Woman)))
    stratified_sample = pd.concat([sample_M, sample_W])  
    print(stratified_sample)