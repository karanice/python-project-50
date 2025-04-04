def format_value(value):
    if isinstance(value, dict): 
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int):
        return str(value)
    elif value is None:
        return 'null'
    else:
        return f'\'{value}\''


def to_plain(diff, prfx=''):
    res_strs = []

    for k, v in diff.items():
        match v["type"]:
            case "added":
                res_strs.append(f'Property \'{prfx}{k}\' '
                               f'was added with value: {format_value(v["value"])}')
            case "removed":
                res_strs.append(f'Property \'{prfx}{k}\' was removed')
            case "updated":
                replace_from = format_value(v["old_value"])
                replace_to = format_value(v["new_value"])
                res_strs.append(f'Property \'{prfx}{k}\' was updated. '
                            f'From {replace_from} to {replace_to}')
            case "nested":
                res_strs.append(to_plain(v["value"], f'{prfx}{k}.'))
    return '\n'.join(res_strs)