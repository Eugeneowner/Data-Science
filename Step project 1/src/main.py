# src/main.py

from __future__ import annotations

from config import (
    FILE_NAME, DATA_URL, TIMEOUT_SEC,
    TOP_N,
    SHOW_PLOTS, SAVE_PLOTS, PLOTS_DIR, DPI,
    CORR_METHOD, STRONG_CORR_THRESHOLD, EXCLUDED_ATTRS, QUALITY_ATTRIBUTES,
    ALT_COL_CANDIDATES, PLOT_XLIM, SCORE_BAND, ALT_BAND, KDE_GRID_SIZE, KDE_SIGMA_BINS,
)

from data.loader import download_if_missing, load_dataset

from tasks.task1_top_countries import run as task1_run
from tasks.task2_correlations import run as task2_run
from tasks.task3_species_color import run as task3_run
from tasks.task4_country_quality import run as task4_run
from tasks.task5_altitude_quality import run as task5_run


def main() -> None:
    download_if_missing(FILE_NAME, DATA_URL, timeout_sec=TIMEOUT_SEC)
    df = load_dataset(FILE_NAME)

    task1_run(
        df,
        top_n=TOP_N,
        save_plots=SAVE_PLOTS,
        show_plots=SHOW_PLOTS,
        plots_dir=PLOTS_DIR,
        dpi=DPI,
    )

    task2_run(
        df,
        attributes=QUALITY_ATTRIBUTES,
        excluded=EXCLUDED_ATTRS,
        threshold=STRONG_CORR_THRESHOLD,
        method=CORR_METHOD,
        save_plots=SAVE_PLOTS,
        show_plots=SHOW_PLOTS,
        plots_dir=PLOTS_DIR,
        dpi=DPI,
    )

    task3_run(
        df,
        save_plots=SAVE_PLOTS,
        show_plots=SHOW_PLOTS,
        plots_dir=PLOTS_DIR,
        dpi=DPI,
    )

    task4_run(
        df,
        top_n=20,
        save_plots=SAVE_PLOTS,
        show_plots=SHOW_PLOTS,
        plots_dir=PLOTS_DIR,
        dpi=DPI,
    )

    task5_run(
        df,
        alt_col_candidates=ALT_COL_CANDIDATES,
        plot_xlim=PLOT_XLIM,
        score_band=SCORE_BAND,
        alt_band=ALT_BAND,
        kde_grid_size=KDE_GRID_SIZE,
        kde_sigma_bins=KDE_SIGMA_BINS,
        save_plots=SAVE_PLOTS,
        show_plots=SHOW_PLOTS,
        plots_dir=PLOTS_DIR,
        dpi=DPI,
    )


if __name__ == "__main__":
    main()