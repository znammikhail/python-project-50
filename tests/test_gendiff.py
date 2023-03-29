# -*- coding:utf-8 -*-
"""Testing modul."""
from gendiff.scripts.gendiff import generate_diff
import pytest


json_1 = "tests/fixtures/file1.json"
json_2 = "tests/fixtures/file2.json"
yaml_1 = "tests/fixtures/file1.yml"
yaml_2 = "tests/fixtures/file2.yml"
file_stylish = "tests/fixtures/file_for_test_stylish.txt"
file_plain = "tests/fixtures/file_for_test_plain.txt"
file_json = "tests/fixtures/file_for_test_json.json"


@pytest.mark.parametrize('path1, path2, format, expected',
                         [(json_1, json_2, 'stylish', file_stylish),
                          (json_1, json_2, 'plain', file_plain),
                          (json_1, json_2, 'json', file_json),
                          (yaml_1, yaml_2, 'stylish', file_stylish),
                          (yaml_1, yaml_2, 'plain', file_plain),
                          (yaml_1, yaml_2, 'json', file_json)])
def test_generate_diff(path1, path2, format, expected):
    """Testing function."""
    with open(expected) as file:
        assert generate_diff(path1, path2, format) == file.read()
