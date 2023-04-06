"""."""
import json


def change_val_to_str(val) -> str:
    """Change value. Return str or [comlplex value] (if val is dict)."""
    if isinstance(val, dict):
        return '[complex value]'
    else:
        return json.dumps(val).replace('"', "'")


def plain(data: dict) -> str:
    """."""
    data_out = plain_recurs(data, nodes=[])
    data_out_str = '\n'.join(filter(lambda x: x != '', data_out))
    return data_out_str


def plain_recurs(data: dict, nodes=None) -> list:
    """Return list."""
    result = []
    if nodes is None:
        nodes = []
    for key, value in data.items():
        state = value['state']
        nodes.append(str(key))
        path = '.'.join(nodes)
        if state == 'node':
            result.extend(plain_recurs(value['value'], nodes))
            nodes = nodes[:-1]  # pop
        elif state == 'unchange':
            result.append("")
        elif state == 'add':
            result.append(f"Property '{path}' was added with value: "
                          f"{change_val_to_str(value['value'])}")
        elif state == 'remove':
            result.append(f"Property '{path}' was removed")
        elif state == 'change':
            val_old = change_val_to_str(value['old'])
            val_new = change_val_to_str(value['new'])
            result.append(f"Property '{path}' was updated. "
                          f"From {val_old} to {val_new}")
        nodes = nodes[:-1]
    return result
