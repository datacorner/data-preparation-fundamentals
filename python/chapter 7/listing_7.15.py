import pandas as pd
import matplotlib.pyplot as plt

# Import common constants and functions
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import common as C

# Define funnel stage classification function
def classify_funnel_stage(orders):
    if orders == 1:
        return 'One-Time Buyer'
    elif orders == 2:
        return 'Repeat Buyer'
    elif orders <= 4:
        return 'Frequent Buyer'
    else:
        return 'Loyal Customer'
    
if __name__ == "__main__":
    df = pd.read_csv(C.DATASET_FOLDER + "superstore/samplesuperstore.csv", encoding='UTF8')

    # Close any existing plots
    plt.close('all')
    
    # Segment Analysis
    segment_analysis = df.groupby(['Customer ID', 'Segment'])['Order ID'].count().reset_index()
    segment_analysis['Funnel Stage'] = segment_analysis['Order ID'].apply(classify_funnel_stage)
    
    # Create crosstab
    segment_funnel = pd.crosstab(
        segment_analysis['Segment'],
        segment_analysis['Funnel Stage'],
        normalize='index'
    ) * 100
    # Create single figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))
    # Plot on the specific axis
    segment_funnel.plot(kind='bar', stacked=True, ax=ax)
    # Set titles and labels
    ax.set_title('Funnel Stages by Customer Segment')
    ax.set_xlabel('Customer Segment')
    ax.set_ylabel('Percentage')
    # Adjust legend
    ax.legend(title='Funnel Stage', bbox_to_anchor=(1.05, 1), loc='upper left')
    # Adjust layout and display
    plt.tight_layout()
    plt.show()
    
    # Print segment funnel percentages
    print(segment_funnel)
