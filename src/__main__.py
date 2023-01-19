import logging.config
from datetime import datetime

import DbOperations
from accessConfig import read_config_file
from accessConfig import update_config_file
from priceTrendCapture import priceCapture

config_contents = read_config_file("config.toml")

with open("src/sql/hist_nav_dim.sql", "r") as sql_ddl:
    sql_query = sql_ddl.read()

backend_stuff = DbOperations.DatabaseOperation(
    config_contents["backend"], "select * from hist_nav_dim"
)
hist_nav = priceCapture(config_contents["fund_list"],
                        nav_hist_start_dt='2023-01-03',
                        nav_hist_end_date='2023-01-04')

# hist_nav = priceCapture(config_contents["fund_list"])

print("---------------------------------------------------------------")
print("*** Starting the application ***")
print("---------------------------------------------------------------")


if config_contents["initial_setup"]["completed"]:
    print("Initial setup completed")
    print(hist_nav.joinFundNAVs())
else:
    print("Requires initial setup")
    # TODO Check table under DB
    if backend_stuff.db_connect():
        print("DB is already available")
        print("Updating ")
        update_config_file(config_contents)

    else:
        print("Connection error")


# backend_stuff.execute_sql()
hist_nav = hist_nav.joinFundNAVs()
backend_stuff.historical_nav_load(hist_nav)
