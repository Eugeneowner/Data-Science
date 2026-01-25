# ============================================================
# Homework: Movies dataset analysis with pandas
# ============================================================

import os
import requests
import pandas as pd

# ============================================================
# SETTINGS
# ============================================================

FILE_NAME = "movies.csv"
DATA_URL = (
    "https://gist.githubusercontent.com/tiangechen/"
    "b68782efa49a16edaf07dc2cdaa855ea/raw/"
    "0c794a9717f18b094eabab2cd6a6b9a226903577/movies.csv"
)

# ============================================================
# 1. DOWNLOAD DATASET (IF NOT EXISTS)
# ============================================================

if not os.path.exists(FILE_NAME):
    response = requests.get(DATA_URL, timeout=60)

    if response.status_code == 200:
        with open(FILE_NAME, "wb") as f:
            f.write(response.content)
        print("movies.csv downloaded successfully")
    else:
        raise RuntimeError(
            f"Failed to download file. Status code: {response.status_code}"
        )
else:
    print("movies.csv already exists")

# ============================================================
# LOAD DATA INTO PANDAS
# ============================================================

# Required: using read_table
df = pd.read_table(FILE_NAME, sep=",")

# Remove duplicate rows
df = df.drop_duplicates()

# ============================================================
# 2. DATA STRUCTURE AND STATISTICS
# ============================================================

print("\n--- Columns ---")
print(df.columns)

print("\n--- Data types ---")
print(df.dtypes)

print("\n--- DataFrame info() ---")
df.info()

print("\n--- DataFrame describe() ---")
print(df.describe())

# ============================================================
# 3. TOTAL NUMBER OF MOVIES (5 METHODS)
# ============================================================

print("\n--- Total number of movies ---")

print("Method 1 (unique):", len(df["Film"].unique()))
print("Method 2 (len):", len(df))
print("Method 3 (count):", df["Film"].count())
print("Method 4 (value_counts):", df["Film"].value_counts().count())
print("Method 5 (shape):", df.shape[0])

# ============================================================
# 4. MOVIES COUNT PER YEAR (5 METHODS)
# ============================================================

print("\n--- Movies per year ---")

print("\nMethod 1 (value_counts):")
print(df["Year"].value_counts().sort_index())

print("\nMethod 2 (groupby + agg):")
print(
    df.groupby("Year")
      .agg(movie_count=("Film", "count"))
      .sort_values("movie_count", ascending=False)
)

print("\nMethod 3 (groupby + count):")
print(df.groupby("Year")["Film"].count())

print("\nMethod 4 (groupby + count + loc):")
print(df.groupby("Year").count().loc[:, ["Film"]])

print("\nMethod 5 (loop):")
for year in sorted(df["Year"].unique()):
    print(f"{year} : {len(df[df['Year'] == year])}")

# ============================================================
# 5. MOST AND LEAST PROFITABLE MOVIES
# ============================================================

print("\n--- Most profitable movie ---")
max_profit = df["Profitability"].max()
print(df[df["Profitability"] == max_profit])

print("\n--- Least profitable movies ---")
min_profit = df["Profitability"].min()
print(df[df["Profitability"] == min_profit])

print("\n--- Alternative (isin) ---")
print(df.loc[df["Profitability"].isin([max_profit, min_profit])])

# ============================================================
# 6. FIX GENRE INCONSISTENCIES
# ============================================================

print("\n--- Unique genres BEFORE ---")
print(df["Genre"].unique())

# Normalize genre values
df["Genre"] = (
    df["Genre"]
    .str.strip()
    .str.lower()
    .replace({
        "romence": "romance",
        "comdy": "comedy"
    })
)

print("\n--- Unique genres AFTER ---")
print(df["Genre"].unique())

# ============================================================
# 7. TOP 10 COMEDIES BY AUDIENCE SCORE
# ============================================================

top_10_comedies = (
    df[df["Genre"] == "comedy"]
    .sort_values("Audience score %", ascending=False)
    .head(10)
    .loc[:, ["Film", "Year", "Lead Studio"]]
)

print("\n--- Top 10 comedies ---")
print(top_10_comedies)

top_10_comedies.to_csv("top_10_comedies.csv", index=False)
print("\nSaved to top_10_comedies.csv")