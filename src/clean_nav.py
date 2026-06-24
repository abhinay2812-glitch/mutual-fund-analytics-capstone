import pandas as pd

# Read file
df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort records
df = df.sort_values(["amfi_code", "date"])

# Remove duplicates
df = df.drop_duplicates()

# Fill missing NAV values
df["nav"] = df["nav"].ffill()

# Remove invalid NAV values
df = df[df["nav"] > 0]

# Save cleaned data
df.to_csv("data/processed/nav_history_cleaned.csv", index=False)

print("NAV history cleaned successfully.")
print(df.head())