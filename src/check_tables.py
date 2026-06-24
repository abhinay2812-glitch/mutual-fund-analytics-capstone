import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

print("\nFACT PERFORMANCE")
print(pd.read_sql("SELECT * FROM fact_performance LIMIT 5", conn).columns)

print("\nFACT TRANSACTIONS")
print(pd.read_sql("SELECT * FROM fact_transactions LIMIT 5", conn).columns)

print("\nDIM FUND")
print(pd.read_sql("SELECT * FROM dim_fund LIMIT 5", conn).columns)

conn.close()