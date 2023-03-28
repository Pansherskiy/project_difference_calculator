#!/usr/bin/env python3
import argparse
import os
from difference_calculator.file_parsers.json_parser import json_generate_diff
from difference_calculator.file_parsers.yaml_parser import yaml_generate_diff


def file_extension(file_path):
    return os.path.splitext(file_path)[1].lower()


def start_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration'
                    ' files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    fst_arg = args.first_file
    sec_arg = args.second_file
    f_ext1 = file_extension(fst_arg)
    f_ext2 = file_extension(sec_arg)
    if f_ext1 == '.json' and f_ext2 == '.json':
        print(json_generate_diff(fst_arg, sec_arg))
    if (f_ext1 == '.yaml' or f_ext1 == '.yml') and \
            (f_ext2 == '.yaml' or f_ext2 == '.yml'):
        print(yaml_generate_diff(fst_arg, sec_arg))
