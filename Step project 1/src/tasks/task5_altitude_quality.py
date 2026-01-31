from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.utils.validate import require_columns
from src.utils.plot import finalize_figure


def _pick_altitude_column(df: pd.DataFrame, candidates: list[str]) -> str:
    for c in candidates:
        if c in df.columns:
            return c
    raise KeyError(
        "Task 5: No altitude column found. Expected one of: "
        f"{candidates}. Available columns: {list(df.columns)}"
    )


def run(
    df: pd.DataFrame,
    *,
    alt_col_candidates: list[str],
    plot_xlim: tuple[float, float],
    score_band: tuple[float, float],
    alt_band: tuple[float, float],
    kde_grid_size: int,
    kde_sigma_bins: float, 
    save_plots: bool,
    show_plots: bool,
    plots_dir: str,
    dpi: int,
) -> None:
    
    # -----------------------------
    # 5) Seaborn KDE
    # -----------------------------

    alt_col = _pick_altitude_column(df, alt_col_candidates)
    require_columns(df, [alt_col, "total_cup_points"], context="Task 5")

    tdf = df[[alt_col, "total_cup_points"]].copy()
    tdf[alt_col] = pd.to_numeric(tdf[alt_col], errors="coerce")
    tdf["total_cup_points"] = pd.to_numeric(tdf["total_cup_points"], errors="coerce")
    tdf = tdf.dropna(subset=[alt_col, "total_cup_points"])
    tdf = tdf[(tdf[alt_col] >= -300) & (tdf[alt_col] <= 6000)]
    tdf = tdf[(tdf["total_cup_points"] >= 0) & (tdf["total_cup_points"] <= 100)]

    if tdf.empty:
        print("\nTask 5: No data left after cleaning. Check altitude column / filters.")
        return

    xmin, xmax = plot_xlim
    ymin, ymax = 60.0, float(tdf["total_cup_points"].max())

    tdf[alt_col] = tdf[alt_col].clip(xmin, xmax)
    tdf["total_cup_points"] = tdf["total_cup_points"].clip(ymin, ymax)

    fig, ax = plt.subplots(figsize=(11, 7))

    sns.kdeplot(
        data=tdf,
        x=alt_col,
        y="total_cup_points",
        fill=True,
        levels=50,
        thresh=0.02,
        gridsize=kde_grid_size,
        cmap="viridis",
        ax=ax,
    )

    ax.set_title("Coffee Quality vs Altitude (2D KDE, cleaned)")
    ax.set_xlabel("Altitude (meters)")
    ax.set_ylabel("Total Cup Points")

    ax.axhline(score_band[0], linestyle="--", linewidth=1)
    ax.axhline(score_band[1], linestyle="--", linewidth=1)
    ax.axvline(alt_band[0], linestyle="--", linewidth=1)
    ax.axvline(alt_band[1], linestyle="--", linewidth=1)

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    fig.tight_layout()
    finalize_figure(
        fig,
        filename="task5_altitude_kde_seaborn.png",
        save_plots=save_plots,
        show_plots=show_plots,
        plots_dir=plots_dir,
        dpi=dpi,
    )