import DbOperations
import logging
import logging.config
from readConfig import Config_dict

config_logs = Config_dict["logging"]

logging.basicConfig(
    format=config_logs["format"],
    datefmt=config_logs["date_format"],
    filename=config_logs["file_name"],
    filemode="w",
)


logger = logging.getLogger(__name__)
logger.setLevel(config_logs["level"])
logger.info("---------------------------------------------------------------")
logger.info("*** Starting the application ***")
logger.info("---------------------------------------------------------------")


backend_stuff = DbOperations.DatabaseOperation(Config_dict["backend"])
print(backend_stuff.db_connect())
# backend_stuff.conn.close()

# print(backend_stuff.conn)
