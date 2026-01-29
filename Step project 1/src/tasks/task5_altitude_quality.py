from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils.validate import require_columns
from utils.plot import finalize_figure
from utils.density import gaussian_blur_2d


def pick_altitude_column(df: pd.DataFrame, candidates: list[str]) -> str:
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
    plot_xlim: tuple[int, int],
    score_band: tuple[int, int],
    alt_band: tuple[int, int],
    kde_grid_size: int,
    kde_sigma_bins: float,
    save_plots: bool,
    show_plots: bool,
    plots_dir: str,
    dpi: int,
) -> None:
    alt_col = pick_altitude_column(df, alt_col_candidates)
    require_columns(df, [alt_col, "total_cup_points"], context="Task 5")

    tdf = df[[alt_col, "total_cup_points"]].copy()
    tdf[alt_col] = pd.to_numeric(tdf[alt_col], errors="coerce")
    tdf["total_cup_points"] = pd.to_numeric(tdf["total_cup_points"], errors="coerce")
    tdf = tdf.dropna(subset=[alt_col, "total_cup_points"])

    # Clean impossible values
    tdf = tdf[(tdf[alt_col] >= -300) & (tdf[alt_col] <= 6000)]
    tdf = tdf[(tdf["total_cup_points"] >= 0) & (tdf["total_cup_points"] <= 100)]

    if tdf.empty:
        print("\nTask 5: No data left after cleaning. Check altitude column / filters.")
        return

    xmin, xmax = plot_xlim
    ymin, ymax = 60.0, float(tdf["total_cup_points"].max())

    x = np.clip(tdf[alt_col].to_numpy(), xmin, xmax)
    y = np.clip(tdf["total_cup_points"].to_numpy(), ymin, ymax)

    hist, _, _ = np.histogram2d(
        x, y,
        bins=kde_grid_size,
        range=[[xmin, xmax], [ymin, ymax]]
    )

    density = gaussian_blur_2d(hist, sigma_bins=kde_sigma_bins)

    fig, ax = plt.subplots(figsize=(11, 7))
    im = ax.imshow(
        density.T,
        origin="lower",
        aspect="auto",
        extent=[xmin, xmax, ymin, ymax],
    )

    ax.set_title("Coffee Quality vs Altitude (KDE-like density, cleaned)")
    ax.set_xlabel("Altitude (meters)")
    ax.set_ylabel("Total Cup Points")

    ax.axhline(score_band[0], linewidth=1)
    ax.axhline(score_band[1], linewidth=1)
    ax.axvline(alt_band[0], linewidth=1)
    ax.axvline(alt_band[1], linewidth=1)

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)

    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label("Density (smoothed counts)")

    fig.tight_layout()
    finalize_figure(
        fig,
        "task5_altitude_kde_like.png",
        save_plots=save_plots,
        show_plots=show_plots,
        plots_dir=plots_dir,
        dpi=dpi,
    )