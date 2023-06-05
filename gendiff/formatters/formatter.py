from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json


def formatter(diff, style):
    match style.lower():
        case 'stylish':
            return stylish(diff).rstrip()
        case 'plain':
            return plain(diff).rstrip()
        case 'json':
            return json(diff).rstrip()
        case _:
            print(f"Format '{style}' missing, choose among formats:"
                  f"\n'stylish'\n'plain'\n'json'")
