from itertools import chain


def fix_key(key_to_fix):
    return key_to_fix.split('(')[0]


def fix_value(value):
    if type(value) is dict:
        addition = '[complex value]'
    elif type(value) is bool:
        addition = str(value).lower()
    elif value is None:
        addition = 'null'
    else:
        addition = f'\'{value}\''
    return addition


def plain(diff, prfx=''):
    res_str = []
    keys = list(chain(diff))
    fixed_keys = [fix_key(key) for key in keys]
    for key in keys:
        if fixed_keys.count(fix_key(key)) < 2:
            if '(added)' in key:
                res_str.append(f'Property \'{prfx}{fix_key(key)}\' '
                               f'was added with value: {fix_value(diff[key])}')
            elif '(removed)' in key:
                res_str.append(f'Property \'{prfx}{fix_key(key)}\' was removed')
            else: 
                if type(diff[key]) is dict:
                    new_prfx = prfx + f'{fix_key(key)}.'
                    res_str.append(plain(diff[key], new_prfx))
                else:
                    continue
        elif type(diff[key] is not dict):
            added = f'{fix_key(key)}(added)'
            rmvd = f'{fix_key(key)}(removed)'
            keys.remove(rmvd)
            replace_from = fix_value(diff[rmvd])
            replace_to = fix_value(diff[added])
            res_str.append(f'Property \'{prfx}{fix_key(key)}\' was updated. '
                           f'From {replace_from} to {replace_to}')

    return '\n'.join(res_str)