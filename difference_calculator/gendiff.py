#!/usr/bin/env python3
import argparse
from difference_calculator.parser import generate_diff


def start_parser():
    parser = argparse.ArgumentParser(description='''
    Compares two configuration files and shows a difference.''')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    first_arg = args.first_file
    second_arg = args.second_file
    print(generate_diff(first_arg, second_arg))
