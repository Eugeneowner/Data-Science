from __future__ import annotations

# Dataset
FILE_NAME = "coffee_ratings.csv"
DATA_URL = (
    "https://raw.githubusercontent.com/rfordatascience/"
    "tidytuesday/master/data/2020/2020-07-07/"
    "coffee_ratings.csv"
)
TIMEOUT_SEC = 60

# Task 1
TOP_N = 10

# Plot behavior:
SHOW_PLOTS = False          # True -> show windows, False -> do not block script
SAVE_PLOTS = True           # True -> save plots to disk (recommended)
PLOTS_DIR = "plots"
DPI = 150

# Task 2
CORR_METHOD = "pearson"
STRONG_CORR_THRESHOLD = 0.65
EXCLUDED_ATTRS = {"sweetness", "uniformity", "clean_cup"}

QUALITY_ATTRIBUTES = [
    "aroma",
    "flavor",
    "aftertaste",
    "acidity",
    "body",
    "balance",
    "total_cup_points",
    "sweetness",
    "uniformity",
    "clean_cup",
]

# Task 5
ALT_COL_CANDIDATES = ["altitude_mean_meters", "altitude_low_meters", "altitude_high_meters"]
PLOT_XLIM = (-300, 2500)          # recommended in assignment
SCORE_BAND = (80, 85)             # horizontal band lines
ALT_BAND = (500, 2000)            # vertical band lines
KDE_GRID_SIZE = 200               # 150–250 ok
KDE_SIGMA_BINS = 1.3              # smoothing in "bin units"