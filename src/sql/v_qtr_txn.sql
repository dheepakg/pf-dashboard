drop view v_fund_qtr_txn;
create  view v_fund_qtr_txn as
select fund_name, yearqtr, sum(purchase_price) as invested  from (
select fund_name, txn_date,
strftime('%Y',txn_date) || case WHEN strftime('%m',txn_date) in ('01','02','03') THEN '01'
WHEN strftime('%m',txn_date) in ('04','05','06') THEN '02'
WHEN strftime('%m',txn_date) in ('07','08','09') THEN '03'
WHEN strftime('%m',txn_date) in ('10','11','12') THEN '04'
END   as yearqtr, purchase_price
from txn_dim)
group by fund_name, yearqtr;
