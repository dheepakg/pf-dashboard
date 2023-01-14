import logging
import logging.config
from readConfig import Config_dict
from datetime import datetime

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

logger = logging.getLogger(__name__)
logger.setLevel(config_logs["level"])


def warn_logs(message: str) -> None:
    logger.warning(message)


def info_logs(message: str) -> None:
    logger.info(message)


def debug_logs(message: str) -> None:
    logger.debug(message)


def error_logs(message: str) -> None:
    logger.error(message)


def fatal_logs(message: str) -> None:
    logger.fatal(message)


warn_logs("something here")
info_logs("something more here")
debug_logs("Something even more")
error_logs("something wrong here")
fatal_logs("something fatal")
