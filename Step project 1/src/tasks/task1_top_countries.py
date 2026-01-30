from __future__ import annotations

import pandas as pd
import matplotlib.pyplot as plt

from src.utils.validate import require_columns, clean_string_column
from src.utils.plot import annotate_barh, finalize_figure


def run(
    df: pd.DataFrame,
    *,
    top_n: int,
    save_plots: bool,
    show_plots: bool,
    plots_dir: str,
    dpi: int,
) -> None:
    col = "country_of_origin"
    require_columns(df, [col], context="Task 1")

    df_clean = clean_string_column(df, col)
    top_countries = df_clean[col].value_counts().head(top_n)

    print(f"\nTop {top_n} countries of origin (by number of samples in this dataset):")
    print(top_countries)

    print(
        "\nNOTE: This ranking is based on the number of records (samples) in the dataset "
        "and should not be interpreted as real export volume."
    )

    top_sorted = top_countries.sort_values()

    fig, ax = plt.subplots(figsize=(10, 6))
    top_sorted.plot(kind="barh", ax=ax)

    ax.set_title(f"Top {top_n} Countries of Origin (by Sample Count)")
    ax.set_xlabel("Number of coffee samples")
    ax.set_ylabel("Country of origin")
    annotate_barh(ax)

    fig.text(
        0.5,
        0.01,
        "NOTE: Sample count ≠ export volume. This reflects dataset representation only.",
        ha="center",
        fontsize=9,
    )

    fig.tight_layout()
    finalize_figure(
        fig,
        "task1_top_countries.png",
        save_plots=save_plots,
        show_plots=show_plots,
        plots_dir=plots_dir,
        dpi=dpi,
    )