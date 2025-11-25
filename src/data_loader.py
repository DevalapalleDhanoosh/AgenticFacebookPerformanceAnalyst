import pandas as pd
import json
import os

def load_csv(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")
    return pd.read_csv(path)

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)