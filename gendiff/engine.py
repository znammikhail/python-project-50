from gendiff.parser import parse
from gendiff.formaters.stylish_format import stylish
from gendiff.formaters.plain_format import plain
from gendiff.formaters.json_format import json_format
from gendiff.gen_tree import gen_diff_tree
import os


def get_format(formater):
    """."""
    formats = {
        'stylish': stylish,
        'plain': plain,
        'json': json_format
    }
    return formats[formater]


def get_format_data(pathfile):
    """."""
    format_data = os.path.splitext(pathfile)[1].lstrip('.')
    return format_data


def get_data(pathfile):
    """Read data. Return str."""
    result = ''
    with open(pathfile) as file:
        for line in file:
            result += line
    return result


def generate_diff(first_file, second_file, formater='stylish'):
    """Cenerat diff.

    Args:
        first_file (str): path to first file
        second_file (str): path to second file
        formater (optional): How to output data. Defaults to stylish.

    Returns:
        str: difference tree
    """
    data_file1 = parse(get_data(first_file), get_format_data(first_file))
    data_file2 = parse(get_data(second_file), get_format_data(second_file))
    tree = gen_diff_tree(data_file1, data_file2)
    formater = get_format(formater)
    file_out = formater(tree)
    return file_out
