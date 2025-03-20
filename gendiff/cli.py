import argparse

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')

parser.add_argument('first_file', type=str)
parser.add_argument('second_file', type=str)
parser.add_argument('-f', '--format', default='stylish', help='set format of output')


def get_args():
    return parser.parse_args()