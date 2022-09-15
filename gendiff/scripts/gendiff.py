# -*- coding:utf-8 -*-
""""""
import os
import argparse
import json
import pathlib


def generate_diff(filepath1, filepath2):
    """Generate difference files."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path_1 = pathlib.Path(dir_path, filepath1)
    file_path_2 = pathlib.Path(dir_path, filepath2)
    file_1 = json.load(open(file_path_1))   # dict
    file_2 = json.load(open(file_path_2))
    file_3 = {}

    for key1 in file_1.keys():
        if key1 in file_2.keys():
            if file_1[key1] == file_2[key1]:
                file_3[f'  {key1}'] = file_1[key1]
            else:
                file_3[f'- {key1}'] = file_1[key1]
                file_3[f'+ {key1}'] = file_2[key1]
        else:
            file_3[f'- {key1}'] = file_1[key1]
    for key2 in file_2.keys():
        if key2 not in file_1.keys():
            file_3[f'+ {key2}'] = file_2[key2]

    file_3 = dict(sorted(file_3.items(), key=lambda item: item[0][2:]))
    return json.dumps((file_3), indent=4)


def main():
    parser = argparse.ArgumentParser(description='Compares two configuration \
        files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    first_file, second_file = args.first_file, args.second_file
    print(generate_diff(first_file, second_file))


if __name__ == '__main__':
    main()
