"""Modul for parsing input filesge."""
import json
import yaml


def parse(data: str, format_data: str) -> dict:
    """Parser data."""
    result = {}
    if format_data == 'json':
        result = json.loads(data)
    elif format_data in ('yaml', 'yml'):
        result = yaml.safe_load(data)
    return result
