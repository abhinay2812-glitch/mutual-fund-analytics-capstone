 -- Query 1: Top 5 funds by AUM
SELECT
scheme_name,
aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Query 2: Average expense ratio
SELECT
AVG(expense_ratio_pct) AS avg_expense_ratio
FROM fact_performance;

-- Query 3: Top 10 funds by 1-year return
SELECT
scheme_name,
return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;

-- Query 4: Transactions by state
SELECT
state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- Query 5: Investment amount by transaction type
SELECT
transaction_type,
SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

-- Query 6: Average AUM by category
SELECT
category,
AVG(aum_crore) AS avg_aum
FROM fact_performance
GROUP BY category;

-- Query 7: Risk grade distribution
SELECT
risk_grade,
COUNT(*) AS total_funds
FROM fact_performance
GROUP BY risk_grade;

-- Query 8: Top 10 maximum drawdown funds
SELECT
scheme_name,
max_drawdown_pct
FROM fact_performance
ORDER BY max_drawdown_pct DESC
LIMIT 10;

-- Query 9: Top fund houses by number of schemes
SELECT
fund_house,
COUNT(*) AS total_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY total_schemes DESC;

-- Query 10: Average SIP amount by category
SELECT
category,
AVG(min_sip_amount)
FROM dim_fund
GROUP BY category;