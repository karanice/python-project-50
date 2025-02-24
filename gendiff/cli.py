import argparse

from gendiff.generate_diff import generate_diff
from gendiff.styles.json import json
from gendiff.styles.plain import plain
from gendiff.styles.stylish import stylish

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')

parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', default='stylish', help='set format of output')
args = parser.parse_args()
# не стала убирать эту строку и передавать напрямую в generate_diff,
# потому что тогда ругается на длину строки


def choose_formatter(diff, format):
    match format:
        case 'stylish':
            return stylish(diff)
        case 'plain':
            return plain(diff)
        case 'json':
            return json(diff)


def print_parser():
    diff = generate_diff(args.first_file, args.second_file)
    format = args.format
    print(choose_formatter(diff, format))