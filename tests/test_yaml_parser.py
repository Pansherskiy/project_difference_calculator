from tests.fixtures.yaml_fixture import yaml_file1, yaml_file2, empty_file # noqa
from difference_calculator.file_parsers.yaml_parser import yaml_generate_diff


def test_yaml_generate_diff(yaml_file1, yaml_file2, empty_file):
    assert yaml_generate_diff(yaml_file1, yaml_file2) == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert yaml_generate_diff(yaml_file2, yaml_file1) == '''{
  + follow: false
    host: hexlet.io
  + proxy: 123.234.53.22
  - timeout: 20
  + timeout: 50
  - verbose: true
}'''
    assert yaml_generate_diff(yaml_file1, yaml_file1) == \
           'The files are identical or you have specified the same file'
    assert yaml_generate_diff(yaml_file1, empty_file) == \
           'There are no differences because one or both files are empty'
