#!/usr/bin/env python3
from gendiff.parser import start_parser
from gendiff.gendiff import generate_diff


def main():
    file1, file2, output_style = start_parser()
    print(generate_diff(file1, file2, output_style))


if __name__ == '__main__':
    main()
