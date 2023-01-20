import sqlite3

import pandas as pd

from src.accessConfig import read_config_file
from src.DbOperations import DatabaseOperation

Config_dict = read_config_file("config.toml")
backend = DatabaseOperation(Config_dict["backend"], "select * from hist_nav_dim;")

print(backend)


def test_dbConnect():
    """
    Checks whether the DB file exists under the repo or not.
    """
    conn_string = backend.db_connect()
    print(conn_string)
    assert "sqlite3.Connection" in str(conn_string)


def test_historical_nav_load():
    conn = sqlite3.connect("data/mutual-fund.db")

    df = pd.DataFrame(
        data={
            "name": ["Microsoft", "Amazon", "Apple", "Netflix", "Google"],
            "major_product": ["OS", "AWS", "iPhone", "TV Shows", "Ads"],
        },
        index=range(5),
    )
    backend.historical_nav_load(df, table_name="test_nav")

    df_from_db = pd.read_sql("select name, major_product from test_nav", conn)
    assert df.equals(df_from_db)
