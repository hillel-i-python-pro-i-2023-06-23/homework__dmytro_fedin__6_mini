from app.services import print_output
from app.services.csv_processor import CsvProcessor
from app.services.json_handler import print_astros_number
from app.services.user_csv_printer import write_csv


def main():
    # 1. Read some file.
    print_output('some_input.txt')
    # 2. Generate users.
    write_csv()
    # 3. Who's here?
    print_astros_number()
    # 4. Print CSV data.
    csv_processor = CsvProcessor()
    csv_processor.print_csv_data()
