import json


def find_first_letter_index(string):
    copy = string[:]
    reduced_copy = copy.strip()
    first_letter = list(reduced_copy)[0]
    return list(string).index(first_letter)


def add_sym(string, seq_to_delete, sym):
    space_to_replace_index = find_first_letter_index(string) - 2
    res_list = list(string.replace(seq_to_delete, ''))
    res_list[space_to_replace_index] = sym
    return ''.join(res_list)


def to_stylish(dict):
    res = ((json.dumps(dict, indent=4)).replace('"', '')).replace(',', '')
    strings = res.split('\n')
    new_strings = []

    for string in strings:
        if '(added)' in string:
            new_string = add_sym(string, '(added)', '+')
        elif '(removed)' in string:
            new_string = add_sym(string, '(removed)', '-')
        elif '(not changed)' in string:
            new_string = string.replace('(not changed)', '')
        else:
            new_string = string
        new_strings.append(new_string)

    return '\n'.join(new_strings)