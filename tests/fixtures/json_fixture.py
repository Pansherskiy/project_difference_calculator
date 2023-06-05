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


@pytest.fixture
def nested_json_file1():
    tmp_file_path = "test_file5.json"
    file = open(tmp_file_path, 'w')
    file.write('''{
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": true,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}''')
    file.close()
    yield tmp_file_path
    os.remove(tmp_file_path)


@pytest.fixture
def nested_json_file2():
    tmp_file_path = "test_file6.json"
    file = open(tmp_file_path, 'w')
    file.write('''{
  "common": {
    "follow": false,
    "setting1": "Value 1",
    "setting3": null,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}''')
    file.close()
    yield tmp_file_path
    os.remove(tmp_file_path)


@pytest.fixture
def simple_json_result1():
    return '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''


@pytest.fixture
def simple_json_result2():
    return '''{
  + follow: false
    host: hexlet.io
  + proxy: 123.234.53.22
  - timeout: 20
  + timeout: 50
  - verbose: true
}'''


@pytest.fixture
def simple_json_result3():
    return '''{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}'''


@pytest.fixture
def simple_json_result4():
    return '''{
  + follow: false
  + host: hexlet.io
  + proxy: 123.234.53.22
  + timeout: 50
}'''


@pytest.fixture
def nested_json_result1():
    return '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''    # noqa W291


@pytest.fixture
def nested_json_result2():
    return '''{
    common: {
      - follow: false
        setting1: Value 1
      + setting2: 200
      - setting3: null
      + setting3: true
      - setting4: blah blah
      - setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: so much
              + wow: 
            }
            key: value
          - ops: vops
        }
    }
    group1: {
      - baz: bars
      + baz: bas
        foo: bar
      - nest: str
      + nest: {
            key: value
        }
    }
  + group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  - group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''    # noqa W291


@pytest.fixture
def nested_json_result3():
    return '''{
  - common: {
        follow: false
        setting1: Value 1
        setting3: null
        setting4: blah blah
        setting5: {
            key5: value5
        }
        setting6: {
            key: value
            ops: vops
            doge: {
                wow: so much
            }
        }
    }
  - group1: {
        foo: bar
        baz: bars
        nest: str
    }
  - group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''


@pytest.fixture
def plain_result1():
    return '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]'''


@pytest.fixture
def plain_result2():
    return '''Property 'common.follow' was removed
Property 'common.setting2' was added with value: 200
Property 'common.setting3' was updated. From null to true
Property 'common.setting4' was removed
Property 'common.setting5' was removed
Property 'common.setting6.doge.wow' was updated. From 'so much' to ''
Property 'common.setting6.ops' was removed
Property 'group1.baz' was updated. From 'bars' to 'bas'
Property 'group1.nest' was updated. From 'str' to [complex value]
Property 'group2' was added with value: [complex value]
Property 'group3' was removed'''


@pytest.fixture
def json_result1():
    return '''[
    {
        "key": "common",
        "children": [
            {
                "key": "follow",
                "value": false,
                "change_type": "added"
            },
            {
                "key": "setting1",
                "value": "Value 1",
                "change_type": "unchanged"
            },
            {
                "key": "setting2",
                "value": 200,
                "change_type": "deleted"
            },
            {
                "key": "setting3",
                "old_value": true,
                "new_value": null,
                "change_type": "plain"
            },
            {
                "key": "setting4",
                "value": "blah blah",
                "change_type": "added"
            },
            {
                "key": "setting5",
                "value": {
                    "key5": "value5"
                },
                "change_type": "added"
            },
            {
                "key": "setting6",
                "children": [
                    {
                        "key": "doge",
                        "children": [
                            {
                                "key": "wow",
                                "old_value": "",
                                "new_value": "so much",
                                "change_type": "plain"
                            }
                        ],
                        "change_type": "nested"
                    },
                    {
                        "key": "key",
                        "value": "value",
                        "change_type": "unchanged"
                    },
                    {
                        "key": "ops",
                        "value": "vops",
                        "change_type": "added"
                    }
                ],
                "change_type": "nested"
            }
        ],
        "change_type": "nested"
    },
    {
        "key": "group1",
        "children": [
            {
                "key": "baz",
                "old_value": "bas",
                "new_value": "bars",
                "change_type": "plain"
            },
            {
                "key": "foo",
                "value": "bar",
                "change_type": "unchanged"
            },
            {
                "key": "nest",
                "old_value": {
                    "key": "value"
                },
                "new_value": "str",
                "change_type": "plain"
            }
        ],
        "change_type": "nested"
    },
    {
        "key": "group2",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        },
        "change_type": "deleted"
    },
    {
        "key": "group3",
        "value": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        },
        "change_type": "added"
    }
]'''


@pytest.fixture
def json_result2():
    return '''[
    {
        "key": "common",
        "children": [
            {
                "key": "follow",
                "value": false,
                "change_type": "deleted"
            },
            {
                "key": "setting1",
                "value": "Value 1",
                "change_type": "unchanged"
            },
            {
                "key": "setting2",
                "value": 200,
                "change_type": "added"
            },
            {
                "key": "setting3",
                "old_value": null,
                "new_value": true,
                "change_type": "plain"
            },
            {
                "key": "setting4",
                "value": "blah blah",
                "change_type": "deleted"
            },
            {
                "key": "setting5",
                "value": {
                    "key5": "value5"
                },
                "change_type": "deleted"
            },
            {
                "key": "setting6",
                "children": [
                    {
                        "key": "doge",
                        "children": [
                            {
                                "key": "wow",
                                "old_value": "so much",
                                "new_value": "",
                                "change_type": "plain"
                            }
                        ],
                        "change_type": "nested"
                    },
                    {
                        "key": "key",
                        "value": "value",
                        "change_type": "unchanged"
                    },
                    {
                        "key": "ops",
                        "value": "vops",
                        "change_type": "deleted"
                    }
                ],
                "change_type": "nested"
            }
        ],
        "change_type": "nested"
    },
    {
        "key": "group1",
        "children": [
            {
                "key": "baz",
                "old_value": "bars",
                "new_value": "bas",
                "change_type": "plain"
            },
            {
                "key": "foo",
                "value": "bar",
                "change_type": "unchanged"
            },
            {
                "key": "nest",
                "old_value": "str",
                "new_value": {
                    "key": "value"
                },
                "change_type": "plain"
            }
        ],
        "change_type": "nested"
    },
    {
        "key": "group2",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        },
        "change_type": "added"
    },
    {
        "key": "group3",
        "value": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        },
        "change_type": "deleted"
    }
]'''
