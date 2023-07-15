import pandas as pd
from app.services.csv_handler import read_csv_content


def get_mean(data_frame: pd.DataFrame)->float:
    mean_value = data_frame.mean()

    return mean_value


def get_cm_from_inches(value: float) -> float:
    cm = value * 2.54
    return cm


def get_kg_from_pounds(value: float) -> float:
    kg = value * 0.453592
    return kg


def get_mean_height() -> float:
    data_frame = read_csv_content()

    mean_height = get_mean(data_frame['Height(Inches)'])
    cm = get_cm_from_inches(mean_height)
    return cm


def get_mean_weight() -> float:
    data_frame = read_csv_content()

    mean_weight = get_mean(data_frame['Weight(Pounds)'])
    kg = get_kg_from_pounds(mean_weight)
    return kg


def print_csv_data()->None:
    height = get_mean_height()
    weight = get_mean_weight()
    print(f'Mean height is {"%.1f" % height} cm. Mean weight is {"%.1f" % weight} kg.')