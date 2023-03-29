# -*- coding:utf-8 -*-
"""Main file for launch."""
from gendiff.cli import cli
from gendiff.engine import generate_diff


def main():
    """General function."""
    first_path, second_path, format = cli()
    file_out = generate_diff(first_path, second_path, format)
    print(file_out)


if __name__ == '__main__':
    main()
