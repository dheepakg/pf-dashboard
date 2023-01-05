import sqlite3
import tomli
import logging
from readConfig import Config_dict

config = Config_dict

logging.basicConfig(
    format=config["logging"]["format"],
    datefmt=config["logging"]["date_format"],
    filename=config["logging"]["file_name"],
    filemode="a",
)

logger = logging.getLogger(__name__)
logger.setLevel(config["logging"]["level"])


class DatabaseOperation:
    def __init__(self, init_config) -> None:
        logger.info("Class invoked - DatabaseOperation")
        self.conn = None
        self.db_file_path = (
            init_config["backend"]["db_file_dir"] + init_config["backend"]["db_file"]
        )
        pass

    def db_connect(self):
        print("inside db_connect")
        logger.info("inside db_connect")

        try:
            self.conn = sqlite3.connect(
                "file:" + self.db_file_path + "?mode=ro", uri=True
            )
            logger.info("DB File Exists")

            return self.conn
        except:
            return self.conn

    # def db_connect(self):

    #     logger.info("inside db_connect")

    #     self.conn = sqlite3.connect(
    #         "file:" + self.db_file_path + "?mode=ro", uri=True
    #     )
    #     logger.info("DB File Exists")

    #     return self.conn
