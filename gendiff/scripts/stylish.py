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


def stylish(file: dict) -> str:
    """."""
    file_out = stringify_recurs(file)
    file_out.append('}')
    file_out.insert(0, '{')
    tru_file_out = []
    for i in file_out:
        if i[:1] != '[':
            el = i.rstrip()
            tru_file_out.append(el)
    file_out_str = '\n'.join(tru_file_out)
    return file_out_str


def stringify_recurs(file: dict, depth=1, result=[]) -> list:
    """Return list."""
    offset = 2
    indent = ' ' * (4 * depth - offset)
    space = ' '
    for key, value in file.items():
        value = check_val(value)
        if key[:2] == '__':
            result.append(f'{indent}  {key[2:]}: {{')
            result.append(f'{(stringify_recurs(value, depth+1, result))}')
            result.append(f"{' ' * 4 * depth}}}")
        elif key[:2] in ('+ ', '- ', '  '):
            if isinstance(value, dict):
                result.append(f'{indent}{key}: {{')
                result.append(f'{(stringify_recurs(value, depth+1, result))}')
                result.append(f"{' ' * 4 * depth}}}")
            else:
                result.append(f'{indent}{key}:{space}{value}')
        else:
            if isinstance(value, dict):
                result.append(f"{' ' * 4 * depth}{key}: {{")
                result.append(f'{(stringify_recurs(value, depth+1, result))}')
                result.append(f"{' ' * 4 * depth}}}")
            else:
                result.append(f"{' ' * 4 * depth}{key}:{space}{value}")
    return result
