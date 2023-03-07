# -*- coding:utf-8 -*-
"""Testing modul."""
import os
import pathlib
from gendiff.scripts.parsing import parser_my
from gendiff.scripts.gendiff import gen_diff_tree
from gendiff.formaters.stylish import stylish


def test_json():
    """Testing json."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path_file_result = pathlib.Path(dir_path, 'fixtures/file_for_test_stylish.txt')
    first_file = pathlib.Path(dir_path, 'fixtures/file1.json')
    second_file = pathlib.Path(dir_path, 'fixtures/file2.json')
    with open(path_file_result, 'r') as file:
        file_result_str = file.read()
    file_out = gen_diff_tree(parser_my(first_file), parser_my(second_file))
    file_out = stylish(file_out)
    assert file_result_str == file_out


def test_yaml():
    """Testing yaml."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path_file_result = pathlib.Path(dir_path, 'fixtures/file_for_test_stylish.txt')
    first_file = pathlib.Path(dir_path, 'fixtures/file1.yml')
    second_file = pathlib.Path(dir_path, 'fixtures/file2.yml')
    with open(path_file_result, 'r') as file:
        file_result_str = file.read()
    file_out = gen_diff_tree(parser_my(first_file), parser_my(second_file))
    file_out = stylish(file_out)
    assert file_result_str == file_out


def test_for_plain():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path_file_result = pathlib.Path(dir_path, 'fixtures/file_for_test_plain.txt')
    first_file = pathlib.Path(dir_path, 'fixtures/file1.json')
    second_file = pathlib.Path(dir_path, 'fixtures/file2.json')
    with open(path_file_result, 'r') as file:
        file_result_str = file.read()
    file_out = gen_diff_tree(parser_my(first_file), parser_my(second_file))
    file_out = stylish(file_out)
    assert file_result_str == file_out
