"""
module for interacting with local storage (json)
"""


import sys
import argparse
import json


FILE_NAME = "schema.json"
JSON_TEMPLATE = {
    "connections": {},
    "access": []
}


def write_file(file_name, data):
    """write to file"""
    with open(file_name, "w") as w_file:
        json.dump(data, w_file)


try:
    with open(FILE_NAME, "r") as r_file:
        data = json.load(r_file)
except FileNotFoundError:
    data = JSON_TEMPLATE
    write_file(FILE_NAME, data)


def create_parser():
    """parse comand line"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--get")
    parser.add_argument("--set")
    parser.add_argument("--val", nargs='+')
    return parser


if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.get:
        path = namespace.get.split('/')
        try:
            print(data[path[0]][path[1]][path[2]])
        except KeyError:
            print('KeyError')
    elif namespace.set:
        path = namespace.set.split('/')
        data[path[0]][path[1]][path[2]] = ' '.join(namespace.val)
        write_file(FILE_NAME, data)
