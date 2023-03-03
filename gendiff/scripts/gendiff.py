# -*- coding:utf-8 -*-
"""Main file for launch."""
import argparse
from gendiff.scripts.parsing import parser_my
from gendiff.scripts.stylish import stylish


def cli():
    """Cli function.Return two filepath."""
    parser = argparse.ArgumentParser(description='Compares two configuration \
        files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    first_file, second_file = args.first_file, args.second_file
    return first_file, second_file


def gen_diff(first_file, second_file, formater=stylish):
    """Cenerat deff.

    Args:
        first_file (str): _description_
        second_file (str): _description_
        formater (optional): _description_. Defaults to stylish.

    Returns:
        str: tree difference
    """
    file_out = gen_diff_tree(parser_my(first_file), parser_my(second_file))
    file_out = formater(file_out)
    return file_out


def gen_diff_tree(file_1, file_2) -> dict:  # dict
    """Difference files."""
    file_3 = {}
    for key1 in file_1.keys():
        if key1 not in file_2.keys():
            file_3[f'- {key1}'] = file_1[key1]  # removed
        else:
            if isinstance(file_1[key1], dict) \
                    and isinstance(file_2[key1], dict):
                file_3[f"__{key1}"] = gen_diff_tree(file_1[key1], file_2[key1])
            elif file_1[key1] == file_2[key1]:
                file_3[f"  {key1}"] = file_1[key1]  # unchanged
            else:
                file_3[f"- {key1}"] = file_1[key1]  # old value
                file_3[f"+ {key1}"] = file_2[key1]  # new value
    for key2 in file_2.keys():  # added
        if key2 not in file_1.keys():
            file_3[f'+ {key2}'] = file_2[key2]
    return dict(sorted(file_3.items(), key=lambda x: x[0][2:]))


def main():
    """General function."""
    first_file, second_file = cli()
    file_out = gen_diff(first_file, second_file)
    print(file_out)
    # with open('diff_out.txt', 'w') as diff_out:
    #     diff_out.write(file_out)


if __name__ == '__main__':
    main()
