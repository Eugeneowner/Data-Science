from __future__ import annotations

import os
import matplotlib.pyplot as plt


def annotate_barh(ax: plt.Axes) -> None:
    for container in ax.containers:
        ax.bar_label(container, padding=3)


def finalize_figure(
    fig: plt.Figure,
    filename: str,
    *,
    save_plots: bool,
    show_plots: bool,
    plots_dir: str,
    dpi: int,
) -> None:
    if save_plots:
        os.makedirs(plots_dir, exist_ok=True)
        path = os.path.join(plots_dir, filename)
        fig.savefig(path, dpi=dpi, bbox_inches="tight")
        print(f"Saved plot: {path}")

    if show_plots:
        plt.show(block=False)
        plt.pause(0.5)
    plt.close(fig)