import argparse

from gendiff.generate_diff import generate_diff
from gendiff.styles.stylish import stylish

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')

parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', help='set format of output')


def print_parser():
    print(stylish(generate_diff(parser.parse_args().first_file, parser.parse_args().second_file)))