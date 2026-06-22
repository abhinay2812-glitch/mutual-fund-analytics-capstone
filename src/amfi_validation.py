import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Extract unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Find codes present in fund_master but missing in nav_history
missing_codes = fund_codes - nav_codes

# Print results
print("\n===== AMFI CODE VALIDATION =====")

if len(missing_codes) == 0:
    print("✅ All AMFI codes in fund_master exist in nav_history.")
else:
    print("❌ Missing AMFI Codes:")
    print(missing_codes)

print("\nTotal Missing Codes:", len(missing_codes))