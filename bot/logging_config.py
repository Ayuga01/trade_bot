import logging
import os


def setup_logger(order_type="general"):
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(order_type)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    log_filename = f"logs/{order_type.lower()}_orders.log"

    file_handler = logging.FileHandler(log_filename)
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger