import sqlite3
import tomli


class DatabaseOperation:
    def __init__(self) -> None:
        pass

    def config_file_exists(self) -> bool:
        try:
            with open("config.toml", mode="rb") as config_file:
                config = tomli.load(config_file)
            self.db_file_path = config["backend"]["db_file"]
            return True
        except:
            print("Config file doesn't exist")
            return False

    def db_connect(self):
        if self.config_file_exists():
            try:
                self.conn = sqlite3.connect(
                    "file:" + self.db_file_path + "?mode=ro", uri=True
                )
                print("DB File Exists")
            except:
                self.conn = sqlite3.connect(self.db_file_path)
                print("DB file created")
            finally:
                return self.conn
