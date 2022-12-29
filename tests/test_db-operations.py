import sqlite3
import tomli
import pytest


def test_config_file_exists():
    with open("config.toml", mode="rb") as config_file:
        assert str(config_file) == "<_io.BufferedReader name='config.toml'>"


@pytest.mark.check_conn
def test_db_connect():
    with open("config.toml", mode="rb") as config_file:
        config = tomli.load(config_file)
        db_file_path = config["backend"]["db_file"]
    conn = sqlite3.connect("file:" + db_file_path + "?mode=ro", uri=True)
    assert "sqlite3.Connection object at" in str(conn)
