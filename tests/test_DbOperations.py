from src.DbOperations import DatabaseOperation
from src.readConfig import Config_dict

backend = DatabaseOperation(Config_dict)

print(backend)


def test_dbConnect():
    conn_string = backend.db_connect()
    print(conn_string)
    assert "sqlite3.Connection" in str(conn_string)
