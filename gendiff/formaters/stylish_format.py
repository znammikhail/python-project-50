"""."""


def check_val(val):
    """Check value."""
    if isinstance(val, bool):
        if val:
            return "true"
        else:
            return "false"
    elif val is None:
        return 'null'
    return val


def chek_dict(val, depth):
    """Check value on dict."""
    if not isinstance(val, dict):
        return val
    result = ["{"]
    for key, value in val.items():
        result.append(f"\n{'  '*(depth)}  "
                      f"{key}: {chek_dict(value, depth+2)}")
    result.append(f"\n{'  '*(depth-1)}}}")
    return ''.join(result)


def stylish(file: dict) -> str:
    """Format dict to stylish.

    Args:
        file (dict): json or yaml like a dict

    Returns:
        str: stylish string
    """
    file_out = string_recurs(file, result=[])
    file_out.insert(0, '{')
    file_out.append('}')
    tru_file_out = []
    for i in file_out:
        if i[:1] != '[':
            el = i.rstrip()
            tru_file_out.append(el)
    file_out_str = '\n'.join(tru_file_out)
    return file_out_str


def string_recurs(file: dict, depth=1, result=[]) -> list:
    """Return list."""
    indent = '  ' * depth
    for key, value in file.items():
        state = value['state']
        if state == 'node':
            result.append(f"{indent}  {key}: {{")
            result.append(f"{string_recurs(value['value'], depth+2, result)}")
            result.append(f"{indent}  }}")
        elif state == 'add':
            result.append(f"{indent}+ {key}: "
                          f"{chek_dict(check_val(value['value']), depth+2)}")
        elif state == 'remove':
            result.append(f"{indent}- {key}: "
                          f"{chek_dict(check_val(value['value']), depth+2)}")
        elif state == 'unchange':
            result.append(f"{indent}  {key}: "
                          f"{chek_dict(check_val(value['value']), depth+2)}")
        elif state == 'change':
            result.append(f"{indent}- {key}: "
                          f"{chek_dict(check_val(value['old']), depth+2)}")
            result.append(f"{indent}+ {key}: "
                          f"{chek_dict(check_val(value['new']), depth+2)}")
    return result
