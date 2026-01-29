from __future__ import annotations

import numpy as np


def gaussian_kernel_1d(sigma: float, radius: int) -> np.ndarray:
    x = np.arange(-radius, radius + 1)
    k = np.exp(-(x ** 2) / (2 * sigma ** 2))
    k /= k.sum()
    return k


def gaussian_blur_2d(hist2d: np.ndarray, sigma_bins: float) -> np.ndarray:
    if sigma_bins <= 0:
        return hist2d

    radius = int(max(2, round(3 * sigma_bins)))
    k = gaussian_kernel_1d(sigma_bins, radius)

    tmp = np.apply_along_axis(lambda m: np.convolve(m, k, mode="same"), axis=1, arr=hist2d)
    out = np.apply_along_axis(lambda m: np.convolve(m, k, mode="same"), axis=0, arr=tmp)
    return out