from __future__ import annotations

import pandas as pd
import matplotlib.pyplot as plt

from utils.validate import require_columns
from utils.plot import finalize_figure


def run(
    df: pd.DataFrame,
    *,
    save_plots: bool,
    show_plots: bool,
    plots_dir: str,
    dpi: int,
) -> None:
    task3_cols = ["species", "color", "total_cup_points"]
    require_columns(df, task3_cols, context="Task 3")

    tdf = df[task3_cols].copy()
    tdf["species"] = tdf["species"].astype("string").str.strip()
    tdf["color"] = tdf["color"].astype("string").str.strip()
    tdf["total_cup_points"] = pd.to_numeric(tdf["total_cup_points"], errors="coerce")
    tdf = tdf.dropna(subset=["species", "color", "total_cup_points"])
    tdf = tdf[(tdf["species"] != "") & (tdf["color"] != "")]

    pivot_tbl = tdf.pivot_table(
        index="species",
        columns="color",
        values="total_cup_points",
        aggfunc="mean",
    )

    print("\nAverage total cup points by species and bean color:")
    print(pivot_tbl)

    fig, ax = plt.subplots(figsize=(10, 6))
    im = ax.imshow(pivot_tbl.values, aspect="auto")

    ax.set_title("Mean Total Cup Points by Species and Bean Color")
    ax.set_xlabel("Bean color")
    ax.set_ylabel("Coffee species")

    ax.set_xticks(range(len(pivot_tbl.columns)))
    ax.set_yticks(range(len(pivot_tbl.index)))
    ax.set_xticklabels(pivot_tbl.columns, rotation=45, ha="right")
    ax.set_yticklabels(pivot_tbl.index)

    for i in range(pivot_tbl.shape[0]):
        for j in range(pivot_tbl.shape[1]):
            val = pivot_tbl.iat[i, j]
            if pd.isna(val):
                continue
            ax.text(j, i, f"{val:.2f}", ha="center", va="center", fontsize=9)

    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label("Average Total Cup Points")

    fig.tight_layout()
    finalize_figure(
        fig,
        "task3_species_color_heatmap.png",
        save_plots=save_plots,
        show_plots=show_plots,
        plots_dir=plots_dir,
        dpi=dpi,
    )