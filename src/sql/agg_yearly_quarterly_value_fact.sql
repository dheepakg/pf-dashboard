CREATE TABLE agg_yearly_quarterly_value_fact(
    id integer primary key AUTOINCREMENT,
    fund_id integer,
    agg_level text, --quarterly or yearly
    agg_level_unit text, --2022Q1 or 2022
    bought_price NUMERIC,
    units NUMERIC,
    nav NUMERIC -- NAV on quarter end or NAV on year end
    );
