import argparse

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.', 
    epilog="And that's how you'd foo a bar")

parser.add_argument('first_file')
parser.add_argument('second_file')  

def parser_print_help():
    argparse.print_help(parser)