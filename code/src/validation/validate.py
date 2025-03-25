import json
import pandas as pd
from utils.data_loader import load_data

def validate_data(data_file, rules_file):
    data = load_data(data_file)
    with open(rules_file, "r") as file:
        rules = json.load(file)

    for rule in rules:
        column, condition = rule["field"], rule["condition"]
        data["Validation"] = data[column].apply(lambda x: eval(condition))

    return data
