# Data Dictionary

## dim_fund

| Column | Description |
|----------|-------------|
| amfi_code | Unique mutual fund identifier |
| fund_house | AMC name |
| scheme_name | Mutual fund scheme |
| category | Equity/Debt |
| sub_category | Large Cap, Mid Cap, etc. |
| plan | Direct/Regular |
| launch_date | Fund launch date |
| benchmark | Benchmark index |
| expense_ratio_pct | Expense ratio percentage |
| exit_load_pct | Exit load percentage |
| min_sip_amount | Minimum SIP amount |
| min_lumpsum_amount | Minimum lumpsum amount |
| fund_manager | Fund manager |
| risk_category | Risk category |

---

## fact_nav

| Column | Description |
|----------|-------------|
| date | NAV date |
| amfi_code | Fund code |
| nav | Net Asset Value |

---

## fact_transactions

| Column | Description |
|----------|-------------|
| investor_id | Investor identifier |
| transaction_date | Transaction date |
| amfi_code | Fund code |
| transaction_type | SIP/Lumpsum/Redemption |
| amount_inr | Investment amount |
| state | Investor state |
| city | Investor city |
| city_tier | Tier of city |
| age_group | Investor age group |
| gender | Investor gender |
| annual_income_lakh | Annual income |
| payment_mode | Payment method |
| kyc_status | KYC status |

---

## fact_performance

| Column | Description |
|----------|-------------|
| return_1yr_pct | 1 year return |
| return_3yr_pct | 3 year return |
| return_5yr_pct | 5 year return |
| sharpe_ratio | Sharpe ratio |
| sortino_ratio | Sortino ratio |
| alpha | Alpha |
| beta | Beta |
| std_dev_ann_pct | Standard deviation |
| max_drawdown_pct | Maximum drawdown |
| aum_crore | Assets under management |
| expense_ratio_pct | Expense ratio |
| risk_grade | Risk grade |