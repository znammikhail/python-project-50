# -*- coding:utf-8 -*-
"""Testing modul."""
from gendiff.scripts.gendiff import generate_diff


def test_json():
    """Testing json."""
    first_path = '../../tests/fixtures/file1.json'
    second_path = '../../tests/fixtures/file2.json'
    file_out = generate_diff(first_path, second_path)
    with open('tests/fixtures/file_for_test_stylish.txt', 'r') as file_test:
        file_test_str = file_test.read()
    assert file_test_str == file_out


# def test_yaml():
#     """Testing yaml."""
#     first_path = '../../tests/fixtures/file1.yml'
#     second_path = '../../tests/fixtures/file2.yml'
#     file_out = generate_diff(first_path, second_path)
#     with open('fixtures/file_for_test_stylish.txt', 'r') as file_test:
#         file_test_str = file_test.read()
#     with open('fixtures/file_for_test_yaml.txt', 'w') as file_my:
#         file_my.write(file_out)
#     assert '{\n' + file_test_str == file_out


def test_for_plain():
    """Testing plain."""
    first_path = '../../tests/fixtures/file1.json'
    second_path = '../../tests/fixtures/file2.json'
    file_out = generate_diff(first_path, second_path, 'plain')
    with open('tests/fixtures/file_for_test_plain.txt', 'r') as file:
        file_result_str = file.read()
    assert file_result_str == file_out
