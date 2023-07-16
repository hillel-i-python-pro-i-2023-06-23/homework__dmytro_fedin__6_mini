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


# def save_file(request, file_path) -> None:
#     with open(file_path, 'wb') as file:
#         for item in request.iter_content(chunk_size=8192):
#             file.write(item)


def get_response(url: str) -> Response | None:
    # file_name = get_filename_from_url(url)

    logger = get_logger()

    try:
        request = requests.get(url)
        logger.info(f'Request successful in {url}')

        # file_path = os.path.join(FILES_INPUT_DIR, file_name)
        # save_file(request, file_path)

        return request

    except requests.exceptions.RequestException as exception:
        logger.error(f'Error: {exception}')

        return None
