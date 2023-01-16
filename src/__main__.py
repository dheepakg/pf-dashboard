import logging.config
from datetime import datetime

import DbOperations
from accessConfig import read_config_file
from accessConfig import update_config_file
from priceTrendCapture import priceCapture

config_contents = read_config_file("config.toml")


backend_stuff = DbOperations.DatabaseOperation(config_contents["backend"])
hist_nav = priceCapture(config_contents["fund_list"])

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


# print(backend_stuff.conn)
