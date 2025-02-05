from gendiff.parser import parse
from gendiff.make_diff_tree import make_diff_tree
from gendiff.styles.stylish import stylish


def generate_diff(file1_path, file2_path): # сюда должен добавляться форматтер??
    file1, file2 = parse(file1_path), parse(file2_path)
    return make_diff_tree(file1, file2)