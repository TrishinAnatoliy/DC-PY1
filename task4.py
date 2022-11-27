import csv
import json

file = "input.csv"


def csv_to_list_dict(file_):

    list_ = []

    with open(file_, encoding='utf-8') as f:
        csvreader = csv.DictReader(f)
        for row in csvreader:
            list_.append(row)

    return list_
    # TODO реализовать конвертер из csv в json


print(json.dumps(csv_to_list_dict(file), indent=4))
