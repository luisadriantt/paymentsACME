import re


def read_parse_file(file_name):
    correct_lines = []
    with open(file_name, "r") as reader:
        line = reader.readline()
        while line != "":
            if validate_info(line.strip()):
                correct_lines.append(line.strip())
            else:
                print("Unformatted line: ", line)
            line = reader.readline()
    return correct_lines


def validate_info(line):
    to_match = re.fullmatch(
        "([A-Z]*)\=((MO|TU|WE|TH|FR|SA|SU)([0-1]\d|[2][0-3])\:([0-5]\d)\-([0-1]\d|[2][0-3])\:([0-5]\d)(\,|))*",
        line)
    return to_match