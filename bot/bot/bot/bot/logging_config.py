import logging

def setup_logger():
    logging.basicConfig(
        filename="trading.log",
        level=logging.INFO,
        format="%(asctime)s %(message)s"
    )
    return logging