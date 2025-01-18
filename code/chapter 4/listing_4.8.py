import pandas as pd

if __name__ == "__main__":
    data = {
        'Feature1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'Feature2': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        'Class': ['A', 'A', 'B', 'B', 'A', 'B', 'B', 'A', 'A', 'B']
    }
    df = pd.DataFrame(data)
    random_sample = df.sample(frac=0.5) 
    print(random_sample)
