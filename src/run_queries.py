import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

queries = [
"""
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5
""",

"""
SELECT AVG(expense_ratio_pct)
FROM fact_performance
""",

"""
SELECT scheme_name, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10
""",

"""
SELECT state, COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC
""",

"""
SELECT transaction_type,
SUM(amount_inr)
FROM fact_transactions
GROUP BY transaction_type
"""
]

for i, query in enumerate(queries, 1):
    print("\n"+"="*60)
    print(f"QUERY {i}")
    print("="*60)
    df = pd.read_sql(query, conn)
    print(df)

conn.close()