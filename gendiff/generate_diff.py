from gendiff.make_diff_tree import make_diff_tree
from gendiff.parser import parse
from gendiff.styles import format_diff
from os.path import splitext


def get_ext(file_path):
    return splitext(file_path)[1]


def generate_diff(file1_path, file2_path, format):
    ext1, ext2 = get_ext(file1_path), get_ext(file2_path)
    file1, file2 = parse(file1_path, ext1), parse(file2_path, ext2)
    return format_diff(make_diff_tree(file1, file2), format)
