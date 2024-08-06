import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def synthetic_dataset_and_sampling(n, num_trials):
    # Create a synthetic dataset with n rows
    df = pd.DataFrame({'value': np.arange(n)})

    proportions_not_selected = []
    for _ in range(num_trials):
        # Sample with replacement
        sampled_df = df.sample(n, replace=True)

        # Determine which samples were not selected
        not_selected = np.setdiff1d(df['value'], sampled_df['value'])

        # Calculate and append the proportion not selected
        proportion_not_selected = len(not_selected) / n
        proportions_not_selected.append(proportion_not_selected)

    # Plot the distribution of proportions not selected
    plt.hist(proportions_not_selected, bins=30, edgecolor='k', alpha=0.7)
    plt.title('Proportion of Points Not Selected in Bootstrap Samples')
    plt.xlabel('Proportion Not Selected')
    plt.ylabel('Frequency')
    plt.show()

# Invoke the function with n=1000 and num_trials=1000
synthetic_dataset_and_sampling(1000, 1000)
