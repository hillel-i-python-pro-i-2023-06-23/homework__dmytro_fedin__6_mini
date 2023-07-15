import requests

from app.loggers.logger import get_logger

json_path = 'http://api.open-notify.org/astros.json'


def get_json():
    return requests.get(json_path)


def get_response():

    response = get_json()
    logger = get_logger()

    if response.status_code == 200:
        json_data = response.json()
        logger.info(f'Response successful in {json_path}')
        # print(json_data['number'])
        print(json_data['number'])
    else:
        logger.info(f'Error in getting response with code {response.status_code}')
