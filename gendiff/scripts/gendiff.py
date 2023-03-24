#!/usr/bin/env python3
import argparse
import json


def bool_lower(arg):
    if arg is True:
        return 'true'
    elif arg is False:
        return 'false'
    else:
        return arg


def generate_diff(first_file, second_file):
    result = '{'
    data1 = json.load(open(first_file))
    data2 = json.load(open(second_file))
    sorted_data_keys = sorted(data1.keys() | data2.keys())
    for key in sorted_data_keys:
        if key in data1 and key in data2 and data1[key] == data2[key]:
            result += f'\n    {key}: {bool_lower(data1[key])}'
        elif key in data1 and key in data2 and data1[key] != data2[key]:
            result += f'\n  - {key}: {bool_lower(data1[key])}'
            result += f'\n  + {key}: {bool_lower(data2[key])}'
        elif key not in data2:
            result += f'\n  - {key}: {bool_lower(data1[key])}'
        else:
            result += f'\n  + {key}: {bool_lower(data2[key])}'
    result += '\n}'
    return result


def start_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration'
                    ' files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


def main():
    start_parser()


if __name__ == '__main__':
    main()
