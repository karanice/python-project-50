from pathlib import Path
from gendiff.generate_diff import generate_diff
from gendiff.styles import format_diff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_to_stylish_plain_json():
    json1 = get_test_data_path('file1.json')
    json2 = get_test_data_path('file2.json')
    expected = read_file('plain_diff_stylish.txt')
    actual = format_diff(generate_diff(json1, json2), 'stylish')

    assert actual == expected


def test_to_stylish_plain_yaml():
    yaml1 = get_test_data_path('file1.yml')
    yaml2 = get_test_data_path('file2.yml')
    expected = read_file('plain_diff_stylish.txt')
    actual = format_diff(generate_diff(yaml1, yaml2), 'stylish')

    assert actual == expected


def test_to_stylish_tree_json():
    tree_json1 = get_test_data_path('file1_tree.json')
    tree_json2 = get_test_data_path('file2_tree.json')
    expected = read_file('tree_diff_stylish.txt')
    actual = format_diff(generate_diff(tree_json1, tree_json2), 'stylish')

    assert actual == expected


def test_to_stylish_tree_yaml():
    tree_yaml1 = get_test_data_path('file1_tree.yml')
    tree_yaml2 = get_test_data_path('file2_tree.yml')
    expected = read_file('tree_diff_stylish.txt')
    actual = format_diff(generate_diff(tree_yaml1, tree_yaml2), 'stylish')

    assert actual == expected


def test_to_plain_tree_json():
    tree_json1 = get_test_data_path('file1_tree.json')
    tree_json2 = get_test_data_path('file2_tree.json')
    expected = read_file('tree_diff_plain.txt')
    actual = format_diff(generate_diff(tree_json1, tree_json2), 'plain')

    assert actual == expected


# def test_to_json_tree_json():
#     tree_json1 = get_test_data_path('file1_tree.json')
#     tree_json2 = get_test_data_path('file2_tree.json')
#     expected = read_file('tree_diff_json.txt')
#     actual = format_diff(generate_diff(tree_json1, tree_json2), 'json')

#     assert actual == expected