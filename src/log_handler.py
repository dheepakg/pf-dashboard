import logging
import logging.config
from accessConfig import Config_dict
from datetime import datetime


class LogIt:
    def __init__(self):
        now = datetime.now()
        YYYYMMDD = str(now.strftime("%Y%m%d-%H%M"))
        print(YYYYMMDD)

        config_logs = Config_dict["logging"]

        logging.basicConfig(
            format=config_logs["format"],
            datefmt=config_logs["date_format"],
            filename="logs/PFDash-" + YYYYMMDD + ".log",
            filemode="a",
        )
        print("Log file name is", "logs/PFDash-" + YYYYMMDD + ".log")
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(config_logs["level"])

    def warn_logs(self, message: str):
        self.logger.warning(message)

    def info_logs(self, message: str) -> None:
        self.logger.info(message)

    def debug_logs(self, message: str) -> None:
        self.logger.debug(message)

    def error_logs(self, message: str) -> None:
        self.logger.error(message)

    def fatal_logs(self, message: str) -> None:
        self.logger.fatal(message)


# now = datetime.now()
# YYYYMMDD = str(now.strftime("%Y%m%d-%H%M"))
# print(YYYYMMDD)


# config_logs = Config_dict["logging"]

# logging.basicConfig(
#     format=config_logs["format"],
#     datefmt=config_logs["date_format"],
#     filename="logs/PFDash-" + YYYYMMDD + ".log",
#     filemode="a",
# )

# logger = logging.getLogger(__name__)
# logger.setLevel(config_logs["level"])


# def warn_logs(message: str) -> None:
#     logger.warning(message)


# def info_logs(message: str) -> None:
#     logger.info(message)


# def debug_logs(message: str) -> None:
#     logger.debug(message)


# def error_logs(message: str) -> None:
#     logger.error(message)


# def fatal_logs(message: str) -> None:
#     logger.fatal(message)


# warn_logs("something here")
# info_logs("something more here")
# debug_logs("Something even more")
# error_logs("something wrong here")
# fatal_logs("something fatal")
