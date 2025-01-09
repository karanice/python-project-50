import argparse
from gendiff.modules.funcs import generate_diff

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')

parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()


def print_parser():
    print(generate_diff(args.first_file, args.second_file))