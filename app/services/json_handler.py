import requests
from app.loggers.logger import get_logger

json_path = 'http://api.open-notify.org/astros.json'


def get_request():
    return requests.get(json_path)


def get_response() -> dict | None:
    response = get_request()
    logger = get_logger()

    if response.status_code == 200:
        json_data = response.json()
        logger.info(f'Response successful in {json_path}')
        return json_data
    else:
        logger.info(f'Error in getting response with code {response.status_code}')
        return None


def print_astros_number() -> None:
    
    json_dict = get_response()
    number_key = 'number'

    if 'number' in json_dict.keys():
        print(f'Number of astros is {json_dict[number_key]}')
    else:
        print('The direct number of astros is unknown but can be got')
