# -*- coding:utf-8 -*-
"""Main file for launch."""
import argparse
from gendiff.scripts.parsing import parser_my
from gendiff.formaters.stylish import stylish
from gendiff.formaters.plain import plain
from gendiff.formaters.json_format import json_format


def cli():
    """Cli function.Return two filepath."""
    parser = argparse.ArgumentParser(description='Compares two configuration \
        files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default='stylish', type=str)
    args = parser.parse_args()
    first_file, second_file, format = \
        args.first_file, args.second_file, args.format
    return first_file, second_file, format


def get_format(format):
    """."""
    formats = {
        'stylish': stylish,
        'plain': plain,
        'json': json_format
    }
    return formats[format]


def generate_diff(first_file, second_file, formater='stylish'):
    """Cenerat deff.

    Args:
        first_file (str): path to first file
        second_file (str): path to second file
        formater (optional): How to output data. Defaults to stylish.

    Returns:
        str: difference tree
    """
    file_out = gen_diff_tree(parser_my(first_file), parser_my(second_file))
    formater = get_format(formater)
    file_out = formater(file_out)
    return file_out


def gen_diff_tree(file_1, file_2) -> dict:  # dict
    """Difference files."""
    file_3 = {}
    for key1 in file_1.keys():
        if key1 not in file_2.keys():
            file_3[key1] = {'state': 'remove', 'value': file_1[key1]}
        else:
            if isinstance(file_1[key1], dict) \
                    and isinstance(file_2[key1], dict):
                file_3[key1] = {'state': 'node',
                                'value': gen_diff_tree(file_1[key1],
                                                       file_2[key1])}
            elif file_1[key1] == file_2[key1]:
                file_3[key1] = {'state': 'unchange',
                                'value': file_1[key1]}
            else:
                file_3[key1] = {'state': 'change',
                                'old': file_1[key1],
                                'new': file_2[key1]}
    for key2 in file_2.keys():
        if key2 not in file_1.keys():
            file_3[key2] = {'state': 'add', 'value': file_2[key2]}
    return dict(sorted(file_3.items()))


def main():
    """General function."""
    first_path, second_path, format = cli()
    file_out = generate_diff(first_path, second_path, format)
    print(file_out)


if __name__ == '__main__':
    main()
