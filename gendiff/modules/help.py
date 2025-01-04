import argparse

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')

parser.add_argument('first_file')
parser.add_argument('second_file')  

def parser_print_help():
    parser.print_help()