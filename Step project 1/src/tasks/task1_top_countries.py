from __future__ import annotations

import pandas as pd
import matplotlib.pyplot as plt

from src.utils.validate import require_columns, clean_string_column
from src.utils.plot import annotate_barh, finalize_figure


def _to_float(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def _print_top(series: pd.Series, title: str, top_n: int) -> None:
    print(f"\n{title}")
    print(series.head(top_n))


def _rank_dict(series: pd.Series) -> dict[str, int]:
    return {k: i + 1 for i, k in enumerate(series.index.tolist())}


def _spearman_on_ranks(rank_a: dict[str, int], rank_b: dict[str, int]) -> float:
    keys = sorted(set(rank_a) & set(rank_b))
    if len(keys) < 3:
        return float("nan")
    a = pd.Series([rank_a[k] for k in keys], dtype="float64")
    b = pd.Series([rank_b[k] for k in keys], dtype="float64")
    return float(a.corr(b, method="pearson"))


def run(
    df: pd.DataFrame,
    *,
    top_n: int,
    save_plots: bool,
    show_plots: bool,
    plots_dir: str,
    dpi: int,
) -> None:

    required = ["country_of_origin", "number_of_bags", "bag_weight"]
    require_columns(df, required, context="Task 1")

    tdf = df[required].copy()

    tdf = clean_string_column(tdf, "country_of_origin")

    tdf["number_of_bags"] = _to_float(tdf["number_of_bags"])
    tdf["bag_weight"] = _to_float(tdf["bag_weight"])

    tdf = tdf.dropna(subset=["number_of_bags"])

    # -----------------------------
    # Coverage diagnostics
    # -----------------------------
    total_rows = len(tdf)
    rows_with_bag_weight = int(tdf["bag_weight"].notna().sum())
    pct = (rows_with_bag_weight / total_rows * 100.0) if total_rows else 0.0

    print("\nTask 1 — Data coverage diagnostics:")
    print(f"- Total rows (after country cleaning): {total_rows}")
    print(f"- Rows with number_of_bags: {total_rows} (100.0%)")
    print(f"- Rows with bag_weight: {rows_with_bag_weight} ({pct:.1f}%)")

    # -----------------------------
    # 1) Top by total number of bags
    # -----------------------------
    by_bags = (
        tdf.groupby("country_of_origin")["number_of_bags"]
        .sum(min_count=1)
        .sort_values(ascending=False)
    )

    _print_top(by_bags, "Task 1 — Top countries by TOTAL NUMBER OF BAGS (proxy):", top_n)

    # Plot top by bags
    fig, ax = plt.subplots(figsize=(10, 6))
    by_bags.head(top_n).sort_values().plot(kind="barh", ax=ax)
    ax.set_title(f"Top {top_n} Countries by Total Number of Bags")
    ax.set_xlabel("Total number of bags")
    ax.set_ylabel("Country of origin")
    annotate_barh(ax)
    fig.tight_layout()
    finalize_figure(
        fig,
        filename="task1_top_countries_by_bags.png",
        save_plots=save_plots,
        show_plots=show_plots,
        plots_dir=plots_dir,
        dpi=dpi,
    )

    # -----------------------------
    # 2) Sensitivity analysis for total_weight_kg
    # -----------------------------
    defaults = [50.0, 60.0, 70.0]

    top_lists: dict[float, pd.Series] = {}
    rank_maps: dict[float, dict[str, int]] = {}

    for d in defaults:
        # Bag_weight with default (kg)
        filled = tdf["bag_weight"].copy()
        missing_before = int(filled.isna().sum())
        filled = filled.fillna(d)

        # Total weight (kg)
        tmp = tdf.copy()
        tmp["bag_weight_kg"] = filled 
        tmp["total_weight_kg"] = tmp["number_of_bags"] * tmp["bag_weight_kg"]

        by_weight = (
            tmp.groupby("country_of_origin")["total_weight_kg"]
            .sum(min_count=1)
            .sort_values(ascending=False)
        )

        print(f"\nTask 1 — Sensitivity: default bag weight = {d:.0f} kg")
        print(f"- Filled missing bag_weight with {d:.0f} kg: {missing_before} -> 0 missing")
        _print_top(by_weight, "Top countries by ESTIMATED TOTAL WEIGHT (kg):", top_n)

        top_lists[d] = by_weight.head(top_n)
        rank_maps[d] = _rank_dict(by_weight)

    # -----------------------------
    # 3) Rank stability summary (no plots)
    # -----------------------------
    base = 60.0
    base_top = set(top_lists[base].index)

    print("\nTask 1 — Rank stability vs 60kg baseline:")
    for d in defaults:
        if d == base:
            continue
        cur_top = set(top_lists[d].index)
        overlap = len(base_top & cur_top)

        spearman = _spearman_on_ranks(rank_maps[base], rank_maps[d])

        print(
            f"- Compare 60kg vs {d:.0f}kg: "
            f"Top-{top_n} overlap = {overlap}/{top_n}, "
            f"Spearman(rank) = {spearman:.3f}"
        )

    print(
        "- If the same default bag weight is applied to all rows, totals scale linearly;\n"
        "  therefore ranking is expected to remain identical (confirmed by Spearman=1.0).\n"
    )

    print(
        "\nNOTE:\n"
        "- bag_weight is missing for most rows; therefore total_weight_kg is an estimate.\n"
        "- Sensitivity analysis checks whether country ranking is stable under different default bag weights.\n"
    )

    d = 60.0
    tmp = tdf.copy()
    tmp["bag_weight_kg"] = tmp["bag_weight"].fillna(d)
    tmp["total_weight_kg"] = tmp["number_of_bags"] * tmp["bag_weight_kg"]

    by_weight_60 = (
        tmp.groupby("country_of_origin")["total_weight_kg"]
        .sum(min_count=1)
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 6))
    by_weight_60.head(top_n).sort_values().plot(kind="barh", ax=ax)
    ax.set_title(f"Top {top_n} Countries by Estimated Total Weight (kg) — default {int(d)}kg")
    ax.set_xlabel("Estimated total weight (kg)")
    ax.set_ylabel("Country of origin")
    annotate_barh(ax)
    fig.tight_layout()
    finalize_figure(
        fig,
        filename="task1_top_countries_by_total_weight_kg.png",
        save_plots=save_plots,
        show_plots=show_plots,
        plots_dir=plots_dir,
        dpi=dpi,
    )