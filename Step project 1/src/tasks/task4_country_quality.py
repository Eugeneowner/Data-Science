from __future__ import annotations

import pandas as pd
import matplotlib.pyplot as plt

from utils.validate import require_columns
from utils.plot import annotate_barh, finalize_figure
from utils.stats import spearman_corr_no_scipy


def run(
    df: pd.DataFrame,
    *,
    top_n: int,
    save_plots: bool,
    show_plots: bool,
    plots_dir: str,
    dpi: int,
) -> None:
    required_cols = ["country_of_origin", "total_cup_points"]
    require_columns(df, required_cols, context="Task 4")

    tdf = df[required_cols].copy()
    tdf["country_of_origin"] = tdf["country_of_origin"].astype("string").str.strip()
    tdf["total_cup_points"] = pd.to_numeric(tdf["total_cup_points"], errors="coerce")
    tdf = tdf.dropna()
    tdf = tdf[tdf["country_of_origin"] != ""]

    country_mean = (
        tdf.groupby("country_of_origin")["total_cup_points"]
        .mean()
        .sort_values(ascending=False)
    )

    country_mean_top = country_mean.head(top_n)

    print(f"\nTop {top_n} countries by average coffee quality (mean total_cup_points):")
    print(country_mean_top)

    fig, ax = plt.subplots(figsize=(10, 7))
    country_mean_top.sort_values().plot(kind="barh", ax=ax)
    ax.set_title("Average Coffee Quality by Country of Origin")
    ax.set_xlabel("Mean Total Cup Points")
    ax.set_ylabel("Country of origin")
    annotate_barh(ax)

    fig.text(
        0.5,
        0.01,
        "Mean total_cup_points per country (top shown for readability).",
        ha="center",
        fontsize=9,
    )

    fig.tight_layout()
    finalize_figure(
        fig,
        "task4_country_mean_quality.png",
        save_plots=save_plots,
        show_plots=show_plots,
        plots_dir=plots_dir,
        dpi=dpi,
    )

    country_rank_by_mean = country_mean.rank(method="average", ascending=True)
    tdf["country_rank"] = tdf["country_of_origin"].map(country_rank_by_mean)

    spearman_corr = spearman_corr_no_scipy(tdf["country_rank"], tdf["total_cup_points"])

    print("\nSpearman correlation analysis (NO scipy):")
    print(f"Spearman(country_rank_by_mean, total_cup_points) = {spearman_corr:.3f}")
    print(
        "\nNOTE:\n"
        "- country_of_origin is categorical, so we use a rank mapping (by mean score).\n"
        "- This is a heuristic association measure, not proof of causality.\n"
        "- Positive value: higher-ranked (by mean) countries tend to have higher sample scores."
    )