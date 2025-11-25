import pandas as pd

def remove_duplicates(df):
    return df.drop_duplicates()

def handle_missing_values(df, method="drop"):
    if method == "drop":
        return df.dropna()
    elif method == "fill_zero":
        return df.fillna(0)
    elif method == "ffill":
        return df.ffill()
    else:
        raise ValueError("Invalid missing value method")