from json import dumps


def format_value(value, depth):
    if isinstance(value, dict): 
        res_strs = dumps(value, indent=4 * (depth + 1)).split('\n')
        N = len(res_strs) - 1
        for i in range(1, N):
            res_strs[i] = f'    {res_strs[i]}'
        res_strs[N] = f'{(depth + 1) * "    "}{res_strs[N]}'
        return '\n'.join(res_strs)
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, int):
        return str(value)
    elif value is None:
        return 'null'
    else:
        return f'{value}'


def to_stylish(diff, depth=0):
    tab = "    " * depth
    raw_res = "{\n"
    for k, v in diff.items():
        match v["type"]:
            case "unchanged":
                raw_res += f'{tab}    {k}: {format_value(v["value"], depth)}\n'
            case "added":
                raw_res += f'{tab}  + {k}: {format_value(v["value"], depth)}\n'
            case "removed":
                raw_res += f'{tab}  - {k}: {format_value(v["value"], depth)}\n'
            case "updated":
                raw_res += f'{tab}  - {k}: {format_value(v["old_value"], depth)}\n'
                raw_res += f'{tab}  + {k}: {format_value(v["new_value"], depth)}\n'
            case "nested":
                raw_res += f'{tab}    {k}: {to_stylish(v["value"], depth + 1)}\n'
    res = (raw_res + tab + "}").replace('\"', '').replace(",", "")
    return res