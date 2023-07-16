import os.path
from app.config import FILES_INPUT_DIR
from app.loggers.logger import get_logger


def print_output(file_name) -> None:
    file_path = os.path.join(FILES_INPUT_DIR, file_name)

    def get_content() -> str:
        if os.path.isfile(file_path):
            with open(file_path) as file:
                content = file.read()
                return content
        else:
            message = f'{FILES_INPUT_DIR} folder read but no such file as {file_name} found'
            get_logger().info(message)
            return message

    def print_content() -> None:
        to_print = get_content()
        print(to_print)

    print_content()
