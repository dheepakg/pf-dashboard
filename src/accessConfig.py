import tomli
import tomli_w


def read_config_file(file_path="Config.toml") -> dict:
    with open(file_path, mode="rb") as config_file:
        config = tomli.load(config_file)
    return config


def update_config_file(contents: dict, file_path="Config.toml") -> None:
    contents["initial_setup"]["completed"] = True
    with open(file_path, mode="wb") as config_file:
        tomli_w.dump(contents, config_file)
