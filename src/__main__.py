import DbOperations
import logging
import logging.config
from readConfig import Config_dict

config = Config_dict

logging.basicConfig(
    format=config["logging"]["format"],
    datefmt=config["logging"]["date_format"],
    filename=config["logging"]["file_name"],
    filemode="w",
)


logger = logging.getLogger(__name__)
logger.setLevel(config["logging"]["level"])
logger.info("---------------------------------------------------------------")
logger.info("*** Starting the application ***")
logger.info("---------------------------------------------------------------")


backend_stuff = DbOperations.DatabaseOperation()
backend_stuff.db_connect()
# backend_stuff.conn.close()

# print(backend_stuff.conn)
