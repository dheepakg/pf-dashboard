import tomli


def read_config_file(file_path) -> dict:
    with open(file_path, mode="rb") as config_file:
        config = tomli.load(config_file)
    return config


Config_dict = read_config_file("config.toml")
