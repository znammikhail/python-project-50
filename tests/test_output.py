# -*- coding:utf-8 -*-
"""Testing modul."""
import os
import pathlib
from gendiff.scripts.parsing import generate_diff_for_yaml


# def test_json():
#     """Testing json."""
#     dir_path = os.path.dirname(os.path.realpath(__file__))
#     path_file = pathlib.Path(dir_path, 'fixtures/file_out_json.txt')
#     file_1 = pathlib.Path(dir_path, 'fixtures/file1.json')
#     file_2 = pathlib.Path(dir_path, 'fixtures/file2.json')
#     with open(path_file, 'r') as file_out:
#         file_out_str = file_out.read()
#     assert file_out_str == str(generate_diff(file_1, file_2))


def test_yaml():
    """Testing yaml."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path_file = pathlib.Path(dir_path, 'fixtures/file_out.txt')
    file_1 = pathlib.Path(dir_path, 'fixtures/file1.yml')
    file_2 = pathlib.Path(dir_path, 'fixtures/file2.yml')
    with open(path_file, 'r') as file_out:
        file_out_str = file_out.read()
    assert file_out_str == str(generate_diff_for_yaml(file_1, file_2))
