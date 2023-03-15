import functools
import logging
import time
from datetime import datetime

from accessConfig import read_config_file

# To capture time taken


config_logs = read_config_file()["logging"]
now = datetime.now()
# YYYYMMDD = str(now.strftime("%Y%m%d-%H%M"))
YYYYMMDD = str(now.strftime("%Y%m%d"))

logging.basicConfig(
    level=config_logs["level"],
    format=config_logs["format"],
    datefmt=config_logs["date_format"],
    filename="logs/PFDash-" + YYYYMMDD + ".log",
    filemode="a",
)


def log_execution(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logging.info(f"Executing {func.__name__}")
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(
            f"Finished execution of {func.__name__}. Took {round(end_time - start_time,5)} seconds to run "
        )

    return wrapper


@log_execution
def sumof_numbers(a, b):
    print(a + b)


sumof_numbers(20, 45)
