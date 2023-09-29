"""
(c) Copyright Jalasoft. 2023

logger.py
    configuration of logger file
"""
import logging
import os
import pathlib
import sys
from datetime import datetime
from logging import handlers
from config.config import ABS_PATH

DEFAULT_LOG_LEVEL = logging.INFO

DEFAULT_LOG_FORMAT = "%(asctime)s UTC %(levelname)-8s %(name)-15s  %(message)s"


def get_logger(name, level=DEFAULT_LOG_LEVEL, log_format=DEFAULT_LOG_FORMAT):
    """
    Configure logging instance
    :param name:
    :param level:         int   number log level
                                logging.DEBUG
                                logging.INFO
                                logging.WARNING
                                logging.ERROR
                                logging.CRITICAL
    :param log_format:
    :return:
    """
    logger = logging.getLogger(name)
    log_file_name = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

    for handler in logger.handlers:
        logger.removeHandler(handler)
    handler = logging.StreamHandler(sys.__stdout__)
    handler.setLevel(level)
    # ABS_PATH = os.path.abspath(__file__ + "../../../")
    # if logs folder there is not exist it wil be created
    pathlib.Path(f"{ABS_PATH}/logs").mkdir(parents=True, exist_ok=True)
    handler_file = handlers.RotatingFileHandler(f"{ABS_PATH}/logs/{log_file_name}.log",
                                                maxBytes=1000000, backupCount=5)
    handler_file.setLevel(level)

    fmt = logging.Formatter(log_format)
    handler.setFormatter(fmt)
    handler_file.setFormatter(fmt)

    logger.addHandler(handler)
    logger.addHandler(handler_file)
    logger.propagate = False

    logger.setLevel(level)

    return logger
