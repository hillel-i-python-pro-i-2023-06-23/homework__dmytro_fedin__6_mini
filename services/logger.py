import logging
import os

from app.config import LOGS_OUTPUT_DIR


def get_logger(log_message):

    logging.basicConfig(
        format='%(asctime)s - %(levelname)s - %(message)s',
        level=logging.INFO,
        datefmt='%m-%d %H-%M',
        filename=os.path.join(LOGS_OUTPUT_DIR, 'app.log'),
        filemode='a',
    )

    my_logger = logging.getLogger(__name__)

    my_logger.info(log_message)

    return my_logger
