CREATE TABLE dim_fund(
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    risk_grade TEXT
);

CREATE TABLE fact_nav(
    date TEXT,
    amfi_code INTEGER,
    nav REAL
);

CREATE TABLE fact_transactions(
    transaction_date TEXT,
    amfi_code INTEGER,
    amount_inr REAL,
    transaction_type TEXT
);

CREATE TABLE fact_performance(
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    expense_ratio_pct REAL
);