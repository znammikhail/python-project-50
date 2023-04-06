"""."""
import json


def json_format(file: dict) -> str:
    """."""
    result = json.dumps(file, indent=4)
    return result
