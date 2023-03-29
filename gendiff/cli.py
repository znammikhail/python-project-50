import argparse


def cli():
    """Cli function.Return two filepath."""
    parser = argparse.ArgumentParser(description='Compares two configuration \
        files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output',
                        default='stylish', type=str)
    args = parser.parse_args()
    first_file, second_file, format = \
        args.first_file, args.second_file, args.format
    return first_file, second_file, format
