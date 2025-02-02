from gendiff.parse_file import parse


def generate_diff(file1_path, file2_path):
    file1, file2 = parse(file1_path), parse(file2_path)
    result = {}
    keys1 = set(file1.keys())
    keys2 = set(file2.keys())

    all_keys = sorted(list(keys1.union(keys2)))

    has1 = keys1.difference(keys2)
    has2 = keys2.difference(keys1)
    have_both = keys1.intersection(keys2)


    # НЕ ПРОХОДИТ ПОСЛЕДНИЙ ТЕСТ!!! (на уровне парсинга)


    for key in all_keys:
        # CЛУЧАИ, В КОТОРЫХ НЕ ИСПОЛЬЗУЕТСЯ РЕКУРСИВНЫЙ МЕХАНИЗМ

        # ключ уникален для первого словаря
        cond1 = (key in has1)
        # ключ уникален для второго словаря
        cond2 = (key in has2)
        # ключ есть в обоих словарях, но только в одном из словарей его значение может быть словарём
        cond3 = (key in have_both and (type(file1[key]) != type(file2[key])))
        # ключ есть в обоих словарях, и его значение нигде не словарь
        cond4 = (key in have_both and (type(file1[key]) != dict and type(file2[key]) != dict))
        if (cond1 or cond2 or cond3 or cond4): # когда нам нужны +/-, написать покрасивее
            if cond1:
                result[f'- {key}'] = file1[key]
            elif cond2:
                result[f'+ {key}'] = file2[key]
            elif file1[key] == file2[key]:
                result[f'  {key}'] = file1[key]
            else:
                result[f'- {key}'] = file1[key]
                result[f'+ {key}'] = file2[key]
                    
        # СЛУЧАИ, В КОТОРЫХ ИСПОЛЬЗУЕТСЯ РЕКУРСИВНЫЙ МЕХАНИЗМ
        # (В ОБЕИХ СЛОВАРЯХ ПОД ОДНИМ И ТЕМ ЖЕ КЛЮЧОМ НАХОДЯТСЯ СЛОВАРИ)
        else:
            result[f'  {key}'] = generate_diff(file1[key], file2[key])

    return result

# надо придумать, как оформить промежуточное представление (возможно, придётся
# вводить аккумулятор, чтобы фиксировать уровень глубины --- а дальше что?)