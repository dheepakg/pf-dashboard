from src.DbOperations import DatabaseOperation
from src.readConfig import Config_dict

backend = DatabaseOperation(Config_dict)

print(backend)


def test_dbConnect():
    assert str(type(Config_dict["backend"]["db_file"])) == "<class 'str'>"
