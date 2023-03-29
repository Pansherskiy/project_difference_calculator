import pytest
import os


@pytest.fixture
def json_file1():
    tmp_file_path = "test_file1.json"
    file = open(tmp_file_path, 'w')
    file.write('''{
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": false
}''')
    file.close()
    yield tmp_file_path
    os.remove(tmp_file_path)


@pytest.fixture
def json_file2():
    tmp_file_path = "test_file2.json"
    file = open(tmp_file_path, 'w')
    file.write('''{
  "timeout": 20,
  "verbose": true,
  "host": "hexlet.io"
}''')
    file.close()
    yield tmp_file_path
    os.remove(tmp_file_path)


@pytest.fixture
def empty_json_file():
    tmp_file_path = "test_file3.json"
    file = open(tmp_file_path, 'w')
    file.write('{}')
    file.close()
    yield tmp_file_path
    os.remove(tmp_file_path)


@pytest.fixture
def empty_file():
    tmp_file_path = "test_file4.json"
    file = open(tmp_file_path, 'w')
    file.write('''''')
    file.close()
    yield tmp_file_path
    os.remove(tmp_file_path)
