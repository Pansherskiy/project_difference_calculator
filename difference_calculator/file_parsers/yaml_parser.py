#!/usr/bin/env python3
import yaml


def bool_lower(arg):
    if arg is True:
        return 'true'
    elif arg is False:
        return 'false'
    else:
        return arg


def gen_diff_for_regular_yaml_files(first_file, second_file):
    result = '{'
    data1 = yaml.safe_load(open(first_file))
    data2 = yaml.safe_load(open(second_file))
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


def yaml_generate_diff(first_file, second_file):
    text_file1 = open(first_file).read()
    text_file2 = open(second_file).read()
    if len(text_file1) == 0 or len(text_file2) == 0:
        return 'There are no differences because one or both files are empty'
    elif text_file1 == text_file2:
        return 'The files are identical or you have specified the same file'
    else:
        return gen_diff_for_regular_yaml_files(first_file, second_file)
