from pathlib import Path
from gendiff.generate_diff import generate_diff
#from gendiff.parse_json import get_json

generate_diff_plain_json = '{'\
'  - follow: false'\
'    host: hexlet.io'\
'  - proxy: 123.234.53.22'\
'  - timeout: 50'\
'  + timeout: 20'\
'  + verbose: true'\
'}'


def test_generate_diff_plain_json():
    assert generate_diff('test_data/file1.json', 'test_data/file2.json') \
        == generate_diff_plain_json


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename

def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_generate_diff_plain_json():
    json1 = get_test_data_path('file1.json')
    json2 = get_test_data_path('file2.json')
    # parsed_json1 = get_json(json1)
    # parsed_json2 = get_json(json2)
    expected = read_file('plain_json_diff.txt')
    actual = generate_diff(json1, json2)

    assert actual == expected


def test_generate_diff_plain_yaml():
    yaml1 = get_test_data_path('file1.yml')
    yaml2 = get_test_data_path('file2.yml')
    expected = read_file('plain_yaml_diff.txt')
    actual = generate_diff(yaml1, yaml2)

    assert actual == expected