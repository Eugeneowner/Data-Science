from __future__ import annotations

from typing import Iterable
import pandas as pd


def require_columns(df: pd.DataFrame, cols: Iterable[str], context: str = "") -> None:
    missing = [c for c in cols if c not in df.columns]
    if missing:
        prefix = f"{context}: " if context else ""
        raise KeyError(
            f"{prefix}Missing columns: {missing}. "
            f"Available columns: {list(df.columns)}"
        )


def clean_string_column(df: pd.DataFrame, col: str) -> pd.DataFrame:
    out = df.copy()
    out[col] = out[col].astype("string").str.strip()
    out = out[out[col].notna() & (out[col] != "")]
    return out