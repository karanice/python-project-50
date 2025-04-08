def make_diff_tree(data1, data2):
    keys = sorted(data1.keys() | data2.keys())
    result = {}
    for key in keys:
        if key not in data2:
            result[key] = {'type': 'removed', 'value': data1[key]}
        elif key not in data1:
            result[key] = {'type': 'added', 'value': data2[key]}

        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {
                'type': 'nested', 'value': make_diff_tree(data1[key],
                                                          data2[key]),
            }

        elif data1[key] != data2[key]:
            result[key] = {'type': 'updated',
                           'old_value': data1[key], 'new_value': data2[key]}
        else:
            result[key] = {'type': 'unchanged', 'value': data1[key]}

    return result