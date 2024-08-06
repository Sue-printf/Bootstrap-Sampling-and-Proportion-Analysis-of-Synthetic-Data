import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def synthetic_dataset_and_sampling(n, num_trials):
    # TODO: Create a synthetic dataset with n rows. Hint: Use np.arange
    df = pd.DataFrame({'value': ___})
    
    proportions_not_selected = []
    for _ in range(num_trials):
        # TODO: Sample with replacement. Hint: Use the sample method with n and replace=True
        sampled_df = df.___
        
        # TODO: Determine which samples were not selected. Hint: Use np.setdiff1d
        not_selected = np.___(df['value'], sampled_df['value'])
        
        # TODO: Calculate and append the proportion not selected
        proportion_not_selected = ___ / n
        proportions_not_selected.append(proportion_not_selected)

    # TODO: Plot the distribution of proportions not selected. Hint: Use plt.hist
    plt.___(proportions_not_selected, bins=30, edgecolor='k', alpha=0.7)
    plt.title('Proportion of Points Not Selected in Bootstrap Samples')
    plt.xlabel('Proportion Not Selected')
    plt.ylabel('Frequency')
    plt.show()

# Invoke the function for a dataset of size 1000 and 1000 trials
synthetic_dataset_and_sampling(1000, 1000)
