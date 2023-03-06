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


def check_on_dict(val, depth):
    """Check value on dict

    Args:
        val (_type_): _description_
        depth (_type_): _description_

    Returns:
        _type_: _description_
    """
    if not isinstance(val, dict):
        return val
    result = ["{"]
    for key, value in val.items():
        result.append(f"\n{'  '*(depth)}  {key}: {check_on_dict(value, depth+2)}")
    result.append(f"\n{'  '*(depth-1)}}}")
    return ''.join(result)


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
    for key, value in file.items():
        state = value['state']
        # value = check_val(value)
        if state == 'node':
            result.append(f"{indent}  {key}: {{")
            result.append(f"{stringify_recurs(value['value'], depth+1, result)}")
            result.append(f"{' ' * 4 * depth}}}")
        elif state == 'add':
            result.append(f"{indent}+ {key}: {check_on_dict(check_val(value['value']), depth+2)}")
        elif state == 'remove':
            result.append(f"{indent}- {key}: {check_on_dict(check_val(value['value']), depth+2)}")
        elif state == 'unchange':
            result.append(f"{indent}  {key}: {check_on_dict(check_val(value['value']), depth+2)}")
        elif state == 'change':
            result.append(f"{indent}- {key}: {check_on_dict(check_val(value['old value']), depth+2)}")
            result.append(f"{indent}+ {key}: {check_on_dict(check_val(value['new value']), depth+2)}")
    return result
