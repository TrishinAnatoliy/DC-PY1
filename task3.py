filename = "output.csv"

headers = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']

rows = [
    ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
]

delimiter = ","

new_line = "\n"


def to_csv_file() -> None:

    with open(filename, "w") as f:

        header_line = delimiter.join(str(header) for header in headers) + new_line
        f.write(header_line)

        for row in rows:
            delimited_row = delimiter.join(str(num) for num in row) + new_line
            f.write(delimited_row)


to_csv_file()


with open(filename) as output_f:
    for line in output_f:
        print(line, end="")
