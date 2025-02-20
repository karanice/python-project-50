def make_diff_tree(file1, file2):
    result = {}
    keys1 = set(file1.keys())
    keys2 = set(file2.keys())

    all_keys = sorted(list(keys1.union(keys2)))

    has1 = keys1.difference(keys2)
    has2 = keys2.difference(keys1)
    common = keys1.intersection(keys2)

    for key in all_keys:

        cond1 = (key in has1)
        cond2 = (key in has2)
        cond3 = (key in common and (type(file1[key]) is not type(file2[key])))
        cond4 = (key in common and not (type(file1[key]) is dict or type(file2[key]) is dict))
        if (cond1 or cond2 or cond3 or cond4):
            if cond1:
                result[f'{key}(removed)'] = file1[key]
            elif cond2:
                result[f'{key}(added)'] = file2[key]
            elif file1[key] == file2[key]:
                result[f'{key}(not changed)'] = file1[key]
            else:
                result[f'{key}(removed)'] = file1[key]
                result[f'{key}(added)'] = file2[key]
        else:
            result[f'{key}(not changed)'] = make_diff_tree(file1[key], file2[key])

    return result