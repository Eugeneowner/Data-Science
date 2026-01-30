from __future__ import annotations

import pandas as pd
import matplotlib.pyplot as plt

from src.utils.validate import require_columns, clean_string_column
from src.utils.plot import annotate_barh, finalize_figure


def plot_heatmap_matplotlib(
    corr: pd.DataFrame,
    title: str,
    filename: str,
    *,
    mask_upper_triangle: bool,
    fmt: str,
    figsize: tuple[int, int],
    cbar_label: str,
    save_plots: bool,
    show_plots: bool,
    plots_dir: str,
    dpi: int,
) -> None:
    data = corr.copy()

    if mask_upper_triangle:
        for i in range(len(data.index)):
            for j in range(len(data.columns)):
                if j > i:
                    data.iat[i, j] = float("nan")

    fig, ax = plt.subplots(figsize=figsize)
    im = ax.imshow(data.values, aspect="equal")

    ax.set_title(title)
    ax.set_xticks(range(len(data.columns)))
    ax.set_yticks(range(len(data.index)))
    ax.set_xticklabels(data.columns, rotation=45, ha="right")
    ax.set_yticklabels(data.index)

    ax.set_xticks([x - 0.5 for x in range(1, len(data.columns))], minor=True)
    ax.set_yticks([y - 0.5 for y in range(1, len(data.index))], minor=True)
    ax.grid(which="minor", linestyle="-", linewidth=0.5)
    ax.tick_params(which="minor", bottom=False, left=False)

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            val = data.iat[i, j]
            if pd.isna(val):
                continue
            ax.text(j, i, format(val, fmt), ha="center", va="center", fontsize=8)

    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label(cbar_label)

    fig.tight_layout()
    finalize_figure(
        fig,
        filename,
        save_plots=save_plots,
        show_plots=show_plots,
        plots_dir=plots_dir,
        dpi=dpi,
    )


def run(
    df: pd.DataFrame,
    *,
    attributes: list[str],
    excluded: set[str],
    threshold: float,
    method: str,
    save_plots: bool,
    show_plots: bool,
    plots_dir: str,
    dpi: int,
) -> None:
    require_columns(df, attributes, context="Task 2")

    quality_df = df[attributes].apply(pd.to_numeric, errors="coerce")
    corr_matrix = quality_df.corr(method=method)

    print("\nFull Pearson correlation matrix:")
    print(corr_matrix)

    plot_heatmap_matplotlib(
        corr_matrix,
        title="Pearson Correlation Matrix (Lower Triangle)",
        filename="task2_corr_full_lower_triangle.png",
        mask_upper_triangle=True,
        fmt=".2f",
        figsize=(11, 9),
        cbar_label="Pearson correlation",
        save_plots=save_plots,
        show_plots=show_plots,
        plots_dir=plots_dir,
        dpi=dpi,
    )

    filtered_attrs = [c for c in attributes if c not in excluded]
    filtered_corr = corr_matrix.loc[filtered_attrs, filtered_attrs]

    strong_corr = filtered_corr.copy()
    for i in range(strong_corr.shape[0]):
        for j in range(strong_corr.shape[1]):
            if i == j:
                continue
            val = strong_corr.iat[i, j]
            if pd.isna(val) or abs(val) < threshold:
                strong_corr.iat[i, j] = float("nan")

    print(f"\nStrong correlations (|r| >= {threshold}), excluded: {', '.join(sorted(excluded))}")
    print(strong_corr)

    plot_heatmap_matplotlib(
        strong_corr,
        title=f"Strong Correlations (|r| ≥ {threshold})",
        filename="task2_corr_strong_only.png",
        mask_upper_triangle=False,
        fmt=".2f",
        figsize=(9, 7),
        cbar_label="Pearson correlation",
        save_plots=save_plots,
        show_plots=show_plots,
        plots_dir=plots_dir,
        dpi=dpi,
    )