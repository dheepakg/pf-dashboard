import logging
import sqlite3
import pandas as pd


from accessConfig import read_config_file

config_contents = read_config_file("config.toml")



class DatabaseOperation:
    """
    This class is used to execute Database actions.
    """

    def __init__(self, init_config, sql_query) -> None:
        self.conn = None
        self.db_file_path = init_config["db_file_dir"] + init_config["db_file"]
        self.sql_query = sql_query

    def db_connect(self):
        """
        To check whether the DB file is available or not. Returns connection object.
        """
        print("inside db_connect", self.db_file_path)

        self.conn = sqlite3.connect("file:" + self.db_file_path + "?mode=ro", uri=True)

        return self.conn

    def execute_sql(self) -> None:
        """
        Executes SQL.
        """
        self.db_connect()
        self.conn.execute(self.sql_query)
        self.conn.commit()
        self.conn.close()

    def historical_nav_load(self, df) -> None:
        """
        To load historical NAV into table
        """
        # conn = self.db_connect()
        conn = sqlite3.connect(self.db_file_path )
        df.to_sql('hist_nav_dim', conn, if_exists='append', index=False)
        conn.commit()
        conn.close()

