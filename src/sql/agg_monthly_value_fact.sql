CREATE TABLE agg_monthly_value_fact(
    id integer primary key AUTOINCREMENT,
    fund_id integer,
    year_month text,
    bought_price NUMERIC,
    units NUMERIC,
    nav_on_month_end NUMERIC, -- NAV on month end
    FOREIGN KEY (fund_id) REFERENCES funds_dim(ID)
    );
