import pandas as pd
from sklearn.utils import resample

if __name__ == "__main__":
    # Sample dataset
    data = {
    'Feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Feature2': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
    'Class': ['A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B']
}
df = pd.DataFrame(data)
n = 3 
systematic_sample = df.iloc[::n] 
print(systematic_sample)