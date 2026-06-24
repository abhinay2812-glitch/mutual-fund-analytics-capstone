import pandas as pd

# Read CSV
df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Standardize transaction types
df["transaction_type"] = df["transaction_type"].str.title()

# Remove invalid amounts
df = df[df["amount_inr"] > 0]

# Convert transaction date
df["transaction_date"] = pd.to_datetime(df["transaction_date"])

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("Transactions cleaned successfully.")
print(df.head())