import os
import requests
from requests import Response

from app.config import FILES_INPUT_DIR
from urllib.parse import urlsplit
from app.loggers.logger import get_logger


def get_filename_from_url(url=None) -> str | None:
    if url is None:
        return None

    urlpath = urlsplit(url).path
    file_name = os.path.basename(urlpath)
    return file_name


def get_response(url: str)-> Response | None:
    fil_name = get_filename_from_url(url)

    logger = get_logger()

    def save_file()->None:
        with open(os.path.join(FILES_INPUT_DIR, fil_name), 'wb') as file:
            for _ in request.iter_content(chunk_size=8192):
                file.write(_)

    try:
        request = requests.get(url)

        logger.info(f'Response successful in {url}')

        save_file()

        return request

    except requests.exceptions.RequestException as exception:
        logger.error(f'Error: {exception}')

        return None




