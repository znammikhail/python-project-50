def gen_diff_tree(file_1, file_2) -> dict:  # dict
    """Difference files."""
    file_3 = {}
    for key1 in file_1.keys():
        if key1 not in file_2.keys():
            file_3[key1] = {'state': 'remove', 'value': file_1[key1]}
        else:
            if isinstance(file_1[key1], dict) \
                    and isinstance(file_2[key1], dict):
                file_3[key1] = {'state': 'node',
                                'value': gen_diff_tree(file_1[key1],
                                                       file_2[key1])}
            elif file_1[key1] == file_2[key1]:
                file_3[key1] = {'state': 'unchange',
                                'value': file_1[key1]}
            else:
                file_3[key1] = {'state': 'change',
                                'old': file_1[key1],
                                'new': file_2[key1]}
    for key2 in file_2.keys():
        if key2 not in file_1.keys():
            file_3[key2] = {'state': 'add', 'value': file_2[key2]}
    return dict(sorted(file_3.items()))
