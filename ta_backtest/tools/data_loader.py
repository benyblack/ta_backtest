import pandas as pd


def from_csv(file_path: str):
    return pd.read_csv(file_path, sep=',')
