import json

file = "input.csv"

# TODO реализовать конвертер из csv в json


def csv_to_list_dict():

    rows = []
    list_ = []
    dict_ = {}

    with open(file) as source:

        for line in source:
            rows.append(line.strip('\n'))

        headers = rows.pop(0).split(",")

        for string in rows:
            row = string.split(",")
            for header in headers:
                dict_.fromkeys(header, row.pop(0))
                list_.append(dict_)
                dict_.clear()

    return list_


print(json.dumps(csv_to_list_dict(), indent=4))
