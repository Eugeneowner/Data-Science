from __future__ import annotations

import pandas as pd


def spearman_corr_no_scipy(x: pd.Series, y: pd.Series) -> float:
    xr = x.rank(method="average")
    yr = y.rank(method="average")
    return float(xr.corr(yr, method="pearson"))