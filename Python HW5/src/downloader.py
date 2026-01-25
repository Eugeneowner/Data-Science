# ============================================================
# Download utilities
# ============================================================

import os
import requests


def download_document(file_name: str, url: str, timeout: int = 60) -> None:
    if os.path.exists(file_name):
        return

    response = requests.get(url, timeout=timeout)
    if response.status_code == 200:
        with open(file_name, "wb") as f:
            f.write(response.content)
    else:
        print(f"Download failed. Status code: {response.status_code}")