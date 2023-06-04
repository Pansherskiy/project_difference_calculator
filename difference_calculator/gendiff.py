#!/usr/bin/env python3
import json
import yaml
import os
from difference_calculator.formatters.formatter import formatter


def generate_diff(first_file, second_file, style='stylish'):
    """
    The function reads JSON and YAML files and returns a list
    of dictionaries with changes and indicating the type of change.
    """
    text_file1 = data_unpacker(first_file)
    text_file2 = data_unpacker(second_file)
    diff = gendiff_engine(text_file1, text_file2)
    if text_file1 == text_file2:
        return 'The files are identical or you have specified the same file'
    else:
        return formatter(diff, style)


def data_unpacker(file_path):
    json_file = file_path.endswith('.json')
    yaml_file = file_path.endswith('.yaml')
    yml_file = file_path.endswith('.yml')
    if os.path.getsize(file_path) == 0:
        raise ValueError('One or both files are empty')
    elif json_file:
        with open(file_path) as json_f:
            json_data = json.load(json_f)
        return json_data
    elif yaml_file or yml_file:
        with open(file_path) as yaml_f:
            yaml_data = yaml.safe_load(yaml_f)
        return yaml_data
    else:
        raise ValueError('Invalid file format. Expected YAML or JSON files.')


def gendiff_engine(data1, data2):
    sorted_data_keys = sorted(data1.keys() | data2.keys())
    diff = []
    for key in sorted_data_keys:
        if key not in data1:
            diff.append({'key': key,
                         'value': data2[key],
                         'change_type': 'added'})
        elif key not in data2:
            diff.append({'key': key,
                         'value': data1[key],
                         'change_type': 'deleted'})
        elif data1[key] == data2[key]:
            diff.append({'key': key,
                         'value': data1[key],
                         'change_type': 'unchanged'})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({'key': key,
                         'children': gendiff_engine(data1[key], data2[key]),
                         'change_type': 'nested'})
        else:
            diff.append({'key': key,
                         'old_value': data1[key],
                         'new_value': data2[key],
                         'change_type': 'plain'})
    return diff
