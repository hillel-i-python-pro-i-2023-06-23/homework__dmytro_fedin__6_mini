import os.path
from app.config import FILES_INPUT_DIR


def print_output(file_name) -> None:

    # file_name = 'some_input.txt'
    file_path = os.path.join(FILES_INPUT_DIR, file_name)

    def get_content() -> str | None:

        if os.path.isfile(file_path):
            with open(file_path) as file:
                content = file.read()
                return content
        else:
            print(f'{FILES_INPUT_DIR} folder read but no such file as {file_name} found')
            return None

    def print_content() -> None:
        to_print = get_content()
        print(to_print)

    print_content()