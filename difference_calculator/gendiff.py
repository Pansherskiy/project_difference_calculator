#!/usr/bin/env python3
import json
import yaml


def generate_diff(first_file, second_file):
    """
    The function reads JSON and YAML files and returns a list
    of dictionaries with changes and indicating the type of change.
    """
    text_file1 = data_unpacker(first_file)
    text_file2 = data_unpacker(second_file)
    if len(text_file1) == 0 or len(text_file2) == 0:
        return 'There are no differences because one or both files are empty'
    elif text_file1 == text_file2:
        return 'The files are identical or you have specified the same file'
    else:
        return gendiff_engine(text_file1, text_file2)


def bool_lower(arg):
    match arg:
        case True:
            return 'true'
        case False:
            return 'false'
        case None:
            return 'null'
        case _:
            return arg


def data_unpacker(file_path):
    json_file = file_path.endswith('.json')
    yaml_file = file_path.endswith('.yaml')
    yml_file = file_path.endswith('.yml')
    if json_file:
        with open(file_path) as json_file:
            json_data = json.load(json_file)
            return json_data
    if yaml_file or yml_file:
        with open(file_path) as yaml_file:
            yaml_data = yaml.safe_load(yaml_file)
            return yaml_data
    else:
        raise ValueError('Invalid file format. Expected YAML or JSON files.')


def gendiff_engine(data1, data2):
    sorted_data_keys = sorted(data1.keys() | data2.keys())
    diff = []
    for key in sorted_data_keys:
        if key not in data1:
            diff.append({'key': key,
                         'value': bool_lower(data2[key]),
                         'change_type': 'added'})
        elif key not in data2:
            diff.append({'key': key,
                         'value': bool_lower(data1[key]),
                         'change_type': 'deleted'})
        elif data1[key] == data2[key]:
            diff.append({'key': key,
                         'value': bool_lower(data1[key]),
                         'change_type': 'unchanged'})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({'key': key,
                         'children': gendiff_engine(data1[key], data2[key]),
                         'change_type': 'nested'})
        else:
            diff.append({'key': key,
                         'old_value': bool_lower(data1[key]),
                         'new_value': bool_lower(data2[key]),
                         'change_type': 'plain'})
    return diff
