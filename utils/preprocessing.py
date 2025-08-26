import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    return df

def prepare_data(file_path):
    df = preprocess_data(file_path)
    # Data already clear
    return df
