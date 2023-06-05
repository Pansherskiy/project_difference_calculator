from tests.fixtures.json_fixture import * # noqa
from tests.fixtures.yaml_fixture import * # noqa
from gendiff.gendiff import generate_diff


def test_generate_diff_for_empty_files(
        json_file1,
        json_file2,
        yaml_file1,
        yaml_file2,
        empty_file
):
    with pytest.raises(ValueError) as error1:
        generate_diff(json_file1, empty_file)
    with pytest.raises(ValueError) as error2:
        generate_diff(empty_file, json_file1)
    with pytest.raises(ValueError) as error3:
        generate_diff(yaml_file1, empty_file)
    with pytest.raises(ValueError) as error4:
        generate_diff(empty_file, yaml_file1)
    assert str(error1.value) == 'One or both files are empty'
    assert str(error2.value) == 'One or both files are empty'
    assert str(error3.value) == 'One or both files are empty'
    assert str(error4.value) == 'One or both files are empty'


def test_generate_diff_for_simple_json_files(
        json_file1,
        json_file2,
        simple_json_result1,
        simple_json_result2,
        simple_json_result3,
        simple_json_result4,
        empty_json_file
):
    assert generate_diff(json_file1, json_file2) == simple_json_result1
    assert generate_diff(json_file2, json_file1) == simple_json_result2
    assert generate_diff(json_file1, empty_json_file) == simple_json_result3
    assert generate_diff(empty_json_file, json_file1) == simple_json_result4
    assert generate_diff(json_file1, json_file1) == \
        'The files are identical or you have specified the same file'
    assert generate_diff(json_file2, json_file2) == \
        'The files are identical or you have specified the same file'


def test_generate_diff_for_nested_json_files(
        nested_json_file1,
        nested_json_file2,
        nested_json_result1,
        nested_json_result2,
        nested_json_result3,
        empty_json_file
):
    assert generate_diff(nested_json_file1, nested_json_file2) == nested_json_result1
    assert generate_diff(nested_json_file2, nested_json_file1) == nested_json_result2
    assert generate_diff(nested_json_file2, empty_json_file) == nested_json_result3


def test_generate_diff_for_simple_yaml_files(
        yaml_file1,
        yaml_file2,
        simple_yaml_result1,
        simple_yaml_result2
):
    assert generate_diff(yaml_file1, yaml_file2) == simple_yaml_result1
    assert generate_diff(yaml_file2, yaml_file1) == simple_yaml_result2
    assert generate_diff(yaml_file1, yaml_file1) == \
        'The files are identical or you have specified the same file'
    assert generate_diff(yaml_file2, yaml_file2) == \
        'The files are identical or you have specified the same file'


def test_generate_diff_for_nested_yaml_files(
        nested_yaml_file1,
        nested_yaml_file2,
        nested_yaml_result1,
        nested_yaml_result2
):
    assert generate_diff(nested_yaml_file1, nested_yaml_file2) == nested_yaml_result1
    assert generate_diff(nested_yaml_file2, nested_yaml_file1) == nested_yaml_result2


def test_generate_diff_plain_format(
        nested_json_file1,
        nested_json_file2,
        nested_yaml_file1,
        nested_yaml_file2,
        plain_result1,
        plain_result2
):
    assert generate_diff(nested_json_file1, nested_json_file2, 'plain') == plain_result1
    assert generate_diff(nested_yaml_file1, nested_yaml_file2, 'plain') == plain_result1
    assert generate_diff(nested_json_file2, nested_json_file1, 'plain') == plain_result2
    assert generate_diff(nested_yaml_file2, nested_yaml_file1, 'plain') == plain_result2


def test_generate_diff_json_format(
        nested_json_file1,
        nested_json_file2,
        json_result1,
        json_result2,
):
    assert generate_diff(nested_json_file1, nested_json_file2, 'json') == json_result1
    assert generate_diff(nested_json_file2, nested_json_file1, 'json') == json_result2
