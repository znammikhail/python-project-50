# -*- coding:utf-8 -*-
"""Main file for launch."""
import argparse
from .parsing import which_one, generate_diff_for_yaml, generate_diff_for_json


def main():
    """General function."""
    parser = argparse.ArgumentParser(description='Compares two configuration \
        files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    first_file, second_file = args.first_file, args.second_file

    if which_one(first_file) == 'json':
        print(generate_diff_for_json(first_file, second_file))
    elif which_one(first_file) == 'yaml':
        print(generate_diff_for_yaml(first_file, second_file))


if __name__ == '__main__':
    main()
