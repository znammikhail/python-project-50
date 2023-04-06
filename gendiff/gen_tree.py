def gen_diff_tree(first: dict, second: dict) -> dict:  # dict
    """Difference files."""
    result = {}
    for key1 in first.keys():
        if key1 not in second.keys():
            result[key1] = {'state': 'remove', 'value': first[key1]}
        elif isinstance(first[key1], dict) \
                and isinstance(second[key1], dict):
            result[key1] = {'state': 'node',
                            'value': gen_diff_tree(first[key1],
                                                   second[key1])}
        elif first[key1] == second[key1]:
            result[key1] = {'state': 'unchange',
                            'value': first[key1]}
        else:
            result[key1] = {'state': 'change',
                            'old': first[key1],
                            'new': second[key1]}
    for key2 in second.keys():
        if key2 not in first.keys():
            result[key2] = {'state': 'add', 'value': second[key2]}
    return dict(sorted(result.items()))
