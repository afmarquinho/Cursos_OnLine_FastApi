import logging


def setup_logging():
    logging.basicConfig(
        filename="app_logs.log",
        filemode="w",
        format="%(asctime)s - %(levelname)s - %(message)s",
        level=logging.DEBUG
    )