import tomli

from src.accessConfig import read_config_file
from src.accessConfig import update_config_file

test_config_file = "tests/config_test.toml"


def test_readConfig():
    """
    Tests the config-reader method.
    """
    result = read_config_file(file_path=test_config_file)
    with open(test_config_file, mode="rb") as config_file:
        test_config = tomli.load(config_file)

    assert result["title"] == test_config["title"]


def test_update_config_file():
    """
    Tests the config-file-updater
    """
    test_config_contents = read_config_file(file_path=test_config_file)

    update_config_file(contents=test_config_contents, file_path=test_config_file)

    test_config_contents = read_config_file(file_path=test_config_file)

    assert test_config_contents["initial_setup"]["completed"] == True
