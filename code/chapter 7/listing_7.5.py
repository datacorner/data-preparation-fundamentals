import pandas as pd
import matplotlib.pyplot as plt

def plot_datapoints(datastore, datastore_filled):
    """
    Plots and compares the original and filled data points for 'Sales' during January 2016.
        This function creates three subplots:
        1. The original sales data before filling missing time points.
        2. A scatter plot showing the added data points (after forward filling).
        3. The sales data after filling missing time points.
    Parameters:
        datastore (pandas.DataFrame): The original DataFrame with missing 'Sales' values.
        datastore_filled (pandas.DataFrame): The DataFrame with forward-filled 'Sales' values.
    Returns:
        None: Displays the plot and prints the number of added points after filling missing values.
    """
    # Filter the data for January 2016
    datastore = datastore[(datastore.index.year == 2016) & (datastore.index.month == 1)]
    datastore_filled = datastore_filled[(datastore_filled.index.year == 2016) & (datastore_filled.index.month == 1)]
    # Identify missing data points before and after forward filling
    missing_before = datastore['Sales'].isna()
    missing_after = datastore_filled['Sales'].isna()
    # Create the figure and subplots
    plt.figure(figsize=(12, 8))
    # Plot original data (before filling)
    plt.subplot(3, 1, 1)
    datastore['Sales'].plot(marker='o', linestyle='-', title='Before Filling Missing Time Points')
    plt.ylabel('Sales')
    # Plot the added data points (after filling missing time points)
    plt.subplot(3, 1, 2)
    filled_points = datastore_filled.index[datastore['Sales'].isna() & datastore_filled['Sales'].notna()]
    plt.title('Added Time Data Points')
    plt.scatter(filled_points, datastore_filled.loc[filled_points, 'Sales'], color='red', label='Filled Points')
    plt.ylabel('Sales')
    # Plot the data after filling missing time points
    plt.subplot(3, 1, 3)
    datastore_filled['Sales'].plot(marker='o', linestyle='-', title='After Filling Missing Time Points')
    plt.ylabel('Sales')
    # Set the same X and Y axis scales for all plots
    min_x = min(datastore.index.min(), datastore_filled.index.min())
    max_x = max(datastore.index.max(), datastore_filled.index.max())
    # Apply the same X limits to all subplots
    for ax in plt.gcf().get_axes():
        ax.set_xlim(min_x, max_x)
    # Set Y limits (same as before)
    min_y = min(datastore['Sales'].min(), datastore_filled['Sales'].min())
    max_y = max(datastore['Sales'].max(), datastore_filled['Sales'].max())
    for ax in plt.gcf().get_axes():
        ax.set_ylim(min_y, max_y)
    # Add a legend to the middle plot
    plt.subplot(3, 1, 2).legend(loc='upper left')
    # Tighten the layout and show the plot
    plt.tight_layout()
    plt.show()

    # Print the number of added points
    print("Number of added points: {}".format(len(filled_points)))
    
if __name__ == "__main__":
    df = pd.read_csv("../data/superstore/samplesuperstore.csv", encoding='UTF8')

    # Convert the 'Order Date' column to datetime
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    # Set 'Order Date' as the index
    df.set_index('Order Date', inplace=True)
    # Sort the index to ensure it is in chronological order
    df.sort_index(inplace=True)

    # Generate a complete daily timeline
    daily_index = pd.date_range(start=df.index.min(), 
                                end=df.index.max(), freq='D')
    # Aggregate data by summing numeric columns and taking the first value for non-numeric columns
    data = df.groupby('Order Date').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Ship Date': 'first',
        'Category': 'first'
    })
    # Reindex the dataset to include all days
    data = data.reindex(daily_index)
    data.index.name = 'Order Date'
    print(data.head())
    
    # Fill missing data using forward filling
    datastore_ffill = data.fillna(method='ffill')
    plot_datapoints(data, datastore_ffill)