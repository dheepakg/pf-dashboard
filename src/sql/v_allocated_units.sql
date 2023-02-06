drop view v_allocated_units;
create  view v_allocated_units as
select txn.fund_name as fund_name,
date(txn.txn_date) as purchase_date,
top_up,
purchase_price,
hist.ppfas as nav,
round(txn.purchase_price/hist.ppfas, 3) as allocated_units
from txn_dim txn
inner join hist_nav_dim hist
on txn.txn_date = hist.date;
