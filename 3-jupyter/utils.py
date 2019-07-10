import numpy as np
import pandas as pd

def make_dummy_dataset(sample_size=20, seed=42):
    """Creates a dummy dataset.
    
    Args:
        sample_size (int, optional): Number of samples in dataset
        seed (int, optional): Seed for random number generator
        
    Returns:
        dataset (pandas.DataFrame object): A dataframe containing the dataset.
    """
    
    np.random.seed(seed)

    heights = np.random.normal(1.70, 0.1, sample_size).astype(np.float32)
    weights = np.random.normal(75, 10, sample_size)
    ages = np.random.uniform(18, 60, sample_size)

    eye_colours = np.array(["Blue", "Brown", "Green", "Other"])
    eyes = np.random.choice(eye_colours, sample_size)
    
    dataset = pd.DataFrame({"Height": heights, "Weight": weights, "Age": ages, "Eye colour": eyes})
    
    return dataset