from __future__ import annotations

import os
import requests
import pandas as pd

__all__ = ["download_if_missing", "load_dataset"]

def download_if_missing(file_name: str, url: str, timeout_sec: int = 60) -> None:
    """Download CSV only if it does not exist locally."""
    if os.path.exists(file_name):
        print(f"{file_name} already exists")
        return

    response = requests.get(url, timeout=timeout_sec)
    response.raise_for_status()

    with open(file_name, "wb") as f:
        f.write(response.content)

    if os.path.getsize(file_name) == 0:
        raise RuntimeError(f"Downloaded file '{file_name}' is empty")

    print(f"{file_name} downloaded successfully")


def load_dataset(file_name: str) -> pd.DataFrame:
    """Load CSV with pandas.read_table (as required), drop duplicates."""
    return (
        pd.read_table(file_name, sep=",", encoding="utf-8")
        .drop_duplicates()
    )