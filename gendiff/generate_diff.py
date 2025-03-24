from os.path import splitext

from gendiff.make_diff_tree import make_diff_tree
from gendiff.parser import parse


def get_ext(file_path):
    return splitext(file_path)[1]


def generate_diff(file1_path, file2_path):
    ext1, ext2 = get_ext(file1_path), get_ext(file2_path)
    file1, file2 = parse(file1_path, ext1), parse(file2_path, ext2)
    return make_diff_tree(file1, file2)
