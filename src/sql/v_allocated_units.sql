-- Gives Units allocated against Fund name

drop view v_allocated_units;
create  view v_allocated_units as
select txn.fund_name as fund_name,
date(txn.txn_date) as purchase_date,
top_up,
purchase_price,
case when txn.fund_name = 'ppfas' then hist.ppfas
     when txn.fund_name = 'nifty50' then hist.nifty50 END as nav,
case when txn.fund_name = 'ppfas' then round(txn.purchase_price/hist.ppfas, 3)
     when txn.fund_name = 'nifty50' then round(txn.purchase_price/hist.nifty50, 3) END as allocated_units
from txn_dim txn
inner join hist_nav_dim hist
on txn.txn_date = hist.date;
