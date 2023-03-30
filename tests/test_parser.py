from tests.fixtures.json_fixture import * # noqa
from tests.fixtures.yaml_fixture import * # noqa
from difference_calculator.parser import generate_diff


def test_generate_diff_for_json_files(json_file1, json_file2, empty_json_file, empty_file):
    assert generate_diff(json_file1, json_file2) == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert generate_diff(json_file2, json_file1) == '''{
  + follow: false
    host: hexlet.io
  + proxy: 123.234.53.22
  - timeout: 20
  + timeout: 50
  - verbose: true
}'''
    assert generate_diff(json_file1, empty_json_file) == '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''
    assert generate_diff(empty_json_file, json_file2) == '''{
  + host: hexlet.io
  + timeout: 20
  + verbose: true
}'''
    assert generate_diff(json_file1, empty_file) == \
           'There are no differences because one or both files are empty'
    assert generate_diff(json_file1, json_file1) == \
           'The files are identical or you have specified the same file'


def test_generate_diff_for_yaml_files(yaml_file1, yaml_file2, empty_file):
    assert generate_diff(yaml_file1, yaml_file2) == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert generate_diff(yaml_file2, yaml_file1) == '''{
  + follow: false
    host: hexlet.io
  + proxy: 123.234.53.22
  - timeout: 20
  + timeout: 50
  - verbose: true
}'''
    assert generate_diff(yaml_file1, yaml_file1) == \
           'The files are identical or you have specified the same file'
    assert generate_diff(yaml_file1, empty_file) == \
           'There are no differences because one or both files are empty'
