#!/usr/bin/env python3
import json
import yaml


def bool_lower(arg):
    if arg is True:
        return 'true'
    elif arg is False:
        return 'false'
    else:
        return arg


def data_unpacker(file_path):
    if file_path.endswith('.json'):
        with open(file_path) as json_file:
            json_data = json.load(json_file)
            return json_data
    if file_path.endswith('.yaml') or file_path.endswith('.yml'):
        with open(file_path) as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
            return yaml_data


def gen_diff_for_non_empty_files(first_file_path, second_file_path):
    data1 = data_unpacker(first_file_path)
    data2 = data_unpacker(second_file_path)
    sorted_data_keys = sorted(data1.keys() | data2.keys())
    result = ''
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
    return f'{{{result}\n}}'


def generate_diff(first_file, second_file):
    text_file1 = open(first_file).read()
    text_file2 = open(second_file).read()
    if len(text_file1) == 0 or len(text_file2) == 0:
        return 'There are no differences because one or both files are empty'
    elif text_file1 == text_file2:
        return 'The files are identical or you have specified the same file'
    else:
        return gen_diff_for_non_empty_files(first_file, second_file)
