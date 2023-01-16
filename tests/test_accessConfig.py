import tomli

from src.accessConfig import read_config_file


def test_readConfig():
    result = read_config_file("config.toml")
    with open("config.toml", mode="rb") as test_config_file:
        test_config = tomli.load(test_config_file)

    assert result["title"] == test_config["title"]
