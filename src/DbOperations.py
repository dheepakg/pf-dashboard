import logging
import sqlite3

import tomli
from accessConfig import read_config_file

config_contents = read_config_file("config.toml")
# config_logs = config_contents["logging"]

# logging.basicConfig(
#     format=config_logs["format"],
#     datefmt=config_logs["date_format"],
#     filename=config_logs["file_name"],
#     filemode="a",
# )

# logger = logging.getLogger(__name__)
# logger.setLevel(config_logs["level"])


class DatabaseOperation:
    """
    This class is used to execute Database actions.
    """

    def __init__(self, init_config, sql_query) -> None:
        # logger.info("Class invoked - DatabaseOperation")
        self.conn = None
        self.db_file_path = init_config["db_file_dir"] + init_config["db_file"]
        self.sql_query = sql_query

    def db_connect(self):
        """
        To check whether the DB file is available or not. Returns connection object.
        """
        print("inside db_connect")
        # logger.info("inside db_connect")

        self.conn = sqlite3.connect("file:" + self.db_file_path + "?mode=ro", uri=True)
        # logger.info("DB File Exists")

        return self.conn

    def execute_sql(self) -> None:
        """
        Executes SQL.
        """
        self.db_connect()
        self.conn.execute(self.sql_query)
        self.conn.commit()
        self.conn.close()
