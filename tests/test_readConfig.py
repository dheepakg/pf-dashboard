from src.readConfig import read_config_file


def test_readConfig():
    result = read_config_file("config.toml")
    assert result["title"] == "Configuration file"
