import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Keep valid expense ratios
df = df[
    (df["expense_ratio_pct"] >= 0.1)
    & (df["expense_ratio_pct"] <= 2.5)
]

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/scheme_performance_cleaned.csv",
    index=False
)

print("Scheme performance cleaned successfully.")
print(df.head())