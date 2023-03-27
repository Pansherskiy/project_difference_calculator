from difference_calculator.gendiff import generate_diff


first_json_file = 'tests/fixtures/file1.json'
second_json_file = 'tests/fixtures/file2.json'
empty_json_file = 'tests/fixtures/file3.json'
empty_file = 'tests/fixtures/file4.json'


def test_generate_diff():
    assert generate_diff(first_json_file, second_json_file) == '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    assert generate_diff(first_json_file, empty_json_file) == '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''
    assert generate_diff(empty_json_file, first_json_file) == '''{
  + follow: false
  + host: hexlet.io
  + proxy: 123.234.53.22
  + timeout: 50
}'''
    assert generate_diff(first_json_file, empty_file) == \
        'There are no differences because one or both files are empty'
    assert generate_diff(first_json_file, first_json_file) == \
        'The files are identical or you have specified the same file'
