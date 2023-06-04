#!/usr/bin/env python3
from difference_calculator.parser import start_parser
from difference_calculator.gendiff import generate_diff


def main():
    file1, file2, output_style = start_parser()
    print(generate_diff(file1, file2, output_style))


if __name__ == '__main__':
    main()
