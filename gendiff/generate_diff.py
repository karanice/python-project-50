import json

from gendiff.parse_json import get_json


def generate_diff(file_1, file_2):
    file1 = get_json(file_1)
    file2 = get_json(file_2)

    result = {}
    keys1 = set(file1.keys())
    keys2 = set(file2.keys())

    all_keys = sorted(list(keys1.union(keys2)))

    has1 = keys1.difference(keys2)
    has2 = keys2.difference(keys1)
    # have_both = keys1.intersection(keys2)
    
    for key in all_keys:
        if key in has1:
            result[f'- {key}'] = file1[key]
        elif key in has2:
            result[f'+ {key}'] = file2[key]
        else:  # elif key in have_both и добавить else с ошибкой например
            if file1[key] == file2[key]:
                result[f'  {key}'] = file1[key]
            else:
                result[f'- {key}'] = file1[key]
                result[f'+ {key}'] = file2[key]

    return ((json.dumps(result, indent=2)).replace('"', '')).replace(',', '')