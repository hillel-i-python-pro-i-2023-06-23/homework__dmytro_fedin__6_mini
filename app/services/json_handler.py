import os.path

import requests

from app.config import FILES_INPUT_DIR
from app.loggers.logger import get_logger

json_path = 'http://api.open-notify.org/astros.json'


def get_response():
    def save_file():
        with open(os.path.join(FILES_INPUT_DIR, 'astros.json'), 'wb') as file:
            for _ in request.iter_content(chunk_size=8192):
                file.write(_)

    request = requests.get(json_path)

    save_file()

    return request


def get_response_data() -> dict | None:
    response = get_response()
    logger = get_logger()

    if response.status_code == 200:
        json_data = response.json()
        logger.info(f'Response successful in {json_path}')
        return json_data
    else:
        logger.info(f'Error in getting response with code {response.status_code}')
        return None


def print_astros_number() -> None:
    json_dict = get_response_data()
    number_key = 'number'

    if 'number' in json_dict.keys():
        print(f'Number of astros is {json_dict[number_key]}')
    else:
        print('The direct number of astros is unknown but can be got')
