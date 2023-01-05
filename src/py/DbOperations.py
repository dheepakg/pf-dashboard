import sqlite3
import tomli
import logging

with open("config.toml", mode="rb") as config_file:
    config = tomli.load(config_file)

logging.basicConfig(
    format=config["logging"]["format"],
    datefmt=config["logging"]["date_format"],
    filename=config["logging"]["file_name"],
    filemode="a",
)

logger = logging.getLogger(__name__)
logger.setLevel(config["logging"]["level"])


class DatabaseOperation:
    def __init__(self) -> None:
        logger.info("Class invoked - DatabaseOperation")
        self.conn = None
        self.db_file_path = ""
        pass

    def config_file_exists(self) -> bool:
        try:
            with open("config.toml", mode="rb") as config_file:
                config = tomli.load(config_file)
            self.db_file_path = config["backend"]["db_file"]
            logger.info("Config file is present")
            return True
        except:
            logger.error("Config file doesn't exist")
            return False

    def db_connect(self):
        print("inside db_connect")
        logger.info("inside db_connect")
        file_present_or_not = self.config_file_exists()
        print("dsdsd", file_present_or_not)
        if file_present_or_not:
            print("insdie if ")
            try:
                self.conn = sqlite3.connect(
                    "file:" + self.db_file_path + "?mode=ro", uri=True
                )
                logger.info("DB File Exists")
            except:
                self.conn = sqlite3.connect(self.db_file_path)
                logger.info("DB file created")
            finally:
                logger.info("Connection established")
                # self.conn.close()
                # return self.conn
