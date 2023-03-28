from difference_calculator.gendiff import file_extension


def test_file_extension():
    assert file_extension('file.txt') == '.txt'
    assert file_extension('main.py') == '.py'
    assert file_extension('gendiff/folder/file.json') == '.json'
