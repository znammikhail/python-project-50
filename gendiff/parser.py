"""Modul for parsing input filesge."""
import json
import yaml


def parse(data, format_file) -> dict:
    """Parser data."""
    result = {}
    if isinstance(data, str):
        if format_file == 'json':
            result = json.loads(data)
        elif format_file in ('yaml', 'yml'):
            result = yaml.safe_loads(data)
        return result
    else:
        if format_file == 'json':
            result = json.load(data)
        elif format_file in ('yaml', 'yml'):
            result = yaml.safe_load(data)
        return result
