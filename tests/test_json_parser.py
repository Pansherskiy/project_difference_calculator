from tests.fixtures.json_fixture import json_file1, json_file2, empty_json_file, empty_file # noqa
from difference_calculator.file_parsers.json_parser import json_generate_diff


def test_json_generate_diff(json_file1, json_file2, empty_json_file, empty_file):
    assert json_generate_diff(json_file1, json_file2) == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert json_generate_diff(json_file2, json_file1) == '''{
  + follow: false
    host: hexlet.io
  + proxy: 123.234.53.22
  - timeout: 20
  + timeout: 50
  - verbose: true
}'''
    assert json_generate_diff(json_file1, empty_json_file) == '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''
    assert json_generate_diff(empty_json_file, json_file2) == '''{
  + host: hexlet.io
  + timeout: 20
  + verbose: true
}'''
    assert json_generate_diff(json_file1, empty_file) == \
           'There are no differences because one or both files are empty'
    assert json_generate_diff(json_file1, json_file1) == \
           'The files are identical or you have specified the same file'
