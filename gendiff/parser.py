import argparse

from gendiff.generate_diff import generate_diff
from gendiff.formatter import default_formatter
from gendiff.parse_file import parse

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')

parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


def print_parser():
    print(default_formatter(generate_diff(args.first_file, args.second_file)))