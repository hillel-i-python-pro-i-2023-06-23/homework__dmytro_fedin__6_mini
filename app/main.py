from app.services import print_output
from app.services.json_handler import get_response
from app.services.user_csv_printer import write_csv


def main():
    print_output('some_input.txt')
    write_csv()
    get_response()
