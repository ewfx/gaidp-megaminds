import pandas as pd
import os
from config import DATA_PATH

def load_data(file_name):
    file_path = os.path.join(DATA_PATH, file_name)
    return pd.read_csv(file_path)

def load_regulations():
    file_path = os.path.join(DATA_PATH, "regulations.txt")
    with open(file_path, "r") as file:
        return file.read()
