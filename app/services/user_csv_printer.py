import pathlib

from app.config import FILES_OUTPUT_DIR
from app.loggers.logger import get_logger
from app.services.user_generator import generate_users, User
import csv

csv_file_path = FILES_OUTPUT_DIR.joinpath('users.csv')


def write_csv(amount: int = 100, csv_file_path: pathlib.Path = None):
    logger = get_logger()
    if csv_file_path is None:
        csv_file_path = FILES_OUTPUT_DIR.joinpath('users.csv')
        logger.info(f'csv_file_path is None. Use default value: {csv_file_path.as_uri()}')

    with open(csv_file_path, 'w', newline='') as csv_file:
        logger.info('Start getting csv file')
        csv_writer = csv.DictWriter(csv_file, fieldnames=User.get_fieldnames())
        csv_writer.writeheader()

        user_generator = generate_users(amount=amount)
        for index, user in enumerate(user_generator, start=1):
            csv_writer.writerow(user.get_dict())
            logger.info(f'Write {index}/{amount} to csv file')

    logger.info('End getting csv file')