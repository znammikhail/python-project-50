"""."""


def check_val(val):
    """Check value."""
    if isinstance(val, bool):
        if val:
            return 'true'
        else:
            return 'false'
    elif val is None:
        return 'null'
    return val


def check_complex(val):
    """Check value."""
    if isinstance(val, dict):
        return '[complex value]'
    elif val in ('null', 'true', 'false') or isinstance(val, (int, float)):
        return val
    else:
        return f"'{val}'"


def plain(file: dict) -> str:
    """."""
    file_out = plain_recurs(file)
    file_out_str = '\n'.join(filter(lambda x: x != '', file_out))
    return file_out_str


def plain_recurs(file: dict, nodes=[]) -> list:
    """Return list."""
    result = []
    for key, value in file.items():
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
                          f"{check_complex(check_val(value['value']))}")
        elif state == 'remove':
            result.append(f"Property '{path}' was removed")
        elif state == 'change':
            val_old = check_complex(check_val(value['old']))
            val_new = check_complex(check_val(value['new']))
            result.append(f"Property '{path}' was updated. "
                          f"From {val_old} to {val_new}")
        nodes = nodes[:-1]
    return result
