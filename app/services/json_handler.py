from app.services.responses import get_response

json_url = 'http://api.open-notify.org/astros.json'


def get_json_data() -> dict | None:
    response = get_response(json_url)

    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:

        return None


def print_astros_number() -> None:
    json_dict = get_json_data()
    number_key = 'number'

    if 'number' in json_dict.keys():
        print(f'Number of astros is {json_dict[number_key]}')
    else:
        print('The direct number of astros is unknown but can be got')
