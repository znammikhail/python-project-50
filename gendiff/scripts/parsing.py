"""Modul for parsing input filesge."""
import os
import json
import pathlib
import yaml


def parser_my(filepath) -> dict:
    """Check format."""
    result = ''
    if pathlib.Path(filepath).suffix == '.json':
        result = parser_json(filepath)
    if pathlib.Path(filepath).suffix in ('.yaml', '.yml'):
        result = parser_yaml(filepath)
    return result


def parser_json(filepath1):
    """Generate difference files."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path_1 = pathlib.Path(dir_path, filepath1)
    file_ = json.load(open(file_path_1))   # dict
    file_ = dict(sorted(file_.items()))
    return file_


def parser_yaml(filepath):
    """Generate difference files."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path_1 = pathlib.Path(dir_path, filepath)
    file_ = yaml.safe_load(open(file_path_1))   # dict
    file_ = dict(sorted(file_.items()))
    return file_
