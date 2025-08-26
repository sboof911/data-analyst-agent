import pandas as pd

def preprocess_data(file_path):
    df = pd.read_csv(file_path)
    return df

def prepare_data(file_path):
    # Data already clear
    df = preprocess_data(file_path)
    file_path = file_path[:file_path.rfind("/")] + "/processed_" + file_path[file_path.rfind("/")+1:]
    df.to_csv(file_path, index=False)
    return file_path
