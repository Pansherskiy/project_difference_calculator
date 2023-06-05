from itertools import chain


def stylish(diff, depth=1):
    lines = []
    spaces, post_spaces = create_indents(depth)
    for item in diff:
        change_type = item['change_type']
        match change_type:
            case 'added':
                lines.append(f'{spaces}+ {item["key"]}: '
                             f'{stringify_value(item["value"], depth)}')
            case 'deleted':
                lines.append(f'{spaces}- {item["key"]}: '
                             f'{stringify_value(item["value"], depth)}')
            case 'unchanged':
                lines.append(f'{spaces}  {item["key"]}: '
                             f'{stringify_value(item["value"], depth)}')
            case 'nested':
                lines.append(f'{spaces}  {item["key"]}: '
                             f'{stylish(item["children"], depth=depth + 1)}')
            case 'plain':
                old_value = f'{spaces}- {item["key"]}: ' \
                            f'{stringify_value(item["old_value"], depth)}\n'
                new_value = f'{spaces}+ {item["key"]}: ' \
                            f'{stringify_value(item["new_value"], depth)}'
                lines.append(old_value + new_value)
    return '\n'.join(chain('{', lines, [post_spaces + '}']))


def stringify_value(item, depth):
    if isinstance(item, dict):
        strings = []
        spacers, post_spacers = create_indents(depth + 1)
        for key, value in item.items():
            strings.append(f'{spacers}  {key}: '
                           f'{stringify_value(value, depth + 1)}')
        return '\n'.join(chain('{', strings, [post_spacers + '}']))
    elif isinstance(item, (bool, type(None))):
        return bool_lower(item)
    else:
        return item


def create_indents(depth, div=' ', indent=4):
    special_char_index = 2 * (2 * depth - 1)
    spaces = div * special_char_index
    post_spaces = div * ((depth - 1) * indent)
    return spaces, post_spaces


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
