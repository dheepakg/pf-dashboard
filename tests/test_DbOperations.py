from src.accessConfig import read_config_file
from src.DbOperations import DatabaseOperation

Config_dict = read_config_file("config.toml")
backend = DatabaseOperation(Config_dict["backend"])

print(backend)


def test_dbConnect():
    conn_string = backend.db_connect()
    print(conn_string)
    assert "sqlite3.Connection" in str(conn_string)
