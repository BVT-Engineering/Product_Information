import pandas as pd
from . import data
import importlib.resources


def get_df_from_file_name(filename):
    """Return a dataframe containing data from specified csv filename"""

    path = importlib.resources.open_text(data, filename)
    return pd.read_csv(path)

def autex_frontier_acoustic_fins():
    """Return a dataframe containing Autex frontier acoustic fin data"""

    path = importlib.resources.open_text(data, "Autex Frontier Acoustic Fins.csv")

    return pd.read_csv(path)

def tracklok():
    """Return a dataframe containing tracklok data"""

    path = importlib.resources.open_text(data, "tracklok.csv")

    return pd.read_csv(path)

def gripple():
    """Return a dataframe containing tracklok data"""

    path = importlib.resources.open_text(data, "Gripple.csv")

    return pd.read_csv(path)

def systems():
    """Return a dataframe containing systems data"""

    path = importlib.resources.open_text(data, "systems.csv")

    return pd.read_csv(path)
