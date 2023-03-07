"""."""
import json


def check_val(file):
    """Check value."""
    change = {
        'None': 'null',
        'True': 'true',
        'False': 'false'
    }
    for key, value in change.items():
        file.replace(key, value)
    return file


def json_format(file: dict) -> str:
    """."""
    result = json.dumps(file, indent=4)
    result = check_val(result)
    return result
