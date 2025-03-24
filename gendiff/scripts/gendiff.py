#!/usr/bin/env python3

from gendiff.cli import get_args
from gendiff.generate_diff import generate_diff
from gendiff.styles import format_diff


def main():
    args = get_args()
    diff = generate_diff(args.first_file, args.second_file)
    res = format_diff(diff, args.format)
    print(res)


if __name__ == '__main__':
    main()