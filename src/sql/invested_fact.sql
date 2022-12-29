CREATE TABLE invested_fact(
    id integer primary key AUTOINCREMENT,
    fund_name text,
    purchase_dt text,
    price_paid NUMERIC,
    units_allocated NUMERIC
    );
