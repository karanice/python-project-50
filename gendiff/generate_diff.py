import json

from gendiff.parse_file import parse


def generate_diff(file_1, file_2):
    file1, file2 = parse(file_1), parse(file_2)

    result = {}
    keys1 = set(file1.keys())
    keys2 = set(file2.keys())

    all_keys = sorted(list(keys1.union(keys2)))

    has1 = keys1.difference(keys2)
    has2 = keys2.difference(keys1)
    
    for key in all_keys:
        if key in has1:
            result[f'- {key}'] = file1[key]
        elif key in has2:
            result[f'+ {key}'] = file2[key]
        else:
            if file1[key] == file2[key]:
                result[f'  {key}'] = file1[key]
            else:
                result[f'- {key}'] = file1[key]
                result[f'+ {key}'] = file2[key]

    return ((json.dumps(result, indent=2)).replace('"', '')).replace(',', '')