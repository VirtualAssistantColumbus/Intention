from datetime import datetime
import logging
import os


def create_logger() -> logging.Logger:
    # Create a custom logger
    logger = logging.getLogger('my_app')
    logger.setLevel(logging.DEBUG)

    # Create a timed rotating file handler to create a new log file every day
    log_directory = os.path.join("__internal", "logs")
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)  # Create the log directory if it does not exist
    log_file_name = os.path.join(log_directory, datetime.now().strftime('%Y_%m_%d_app_log.txt'))
    file_handler = logging.FileHandler(log_file_name, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)  # Set the desired log level for file output

    # Create a stream handler for displaying log messages in the terminal
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)

    # Create formatters and add them to the handlers
    file_formatter = logging.Formatter('\n[%(asctime)s] [%(levelname)s] [%(filename)s -> %(funcName)s() -> %(lineno)d]\n%(message)s')
    file_handler.setFormatter(file_formatter)

    stream_formatter= logging.Formatter('\n[%(filename)s -> %(funcName)s() -> %(lineno)d]\n%(message)s')
    stream_handler.setFormatter(stream_formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    return logger