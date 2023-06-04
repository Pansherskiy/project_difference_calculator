from difference_calculator.formatters.stylish import bool_lower


def plain(diff, path_string=''):
    lines = []
    for item in diff:
        change_type = item['change_type']
        path = path_string + item['key']
        match change_type:
            case 'added':
                lines.append(f"Property '{path}' was added with value: "
                             f'{stringify_value(item["value"])}')
            case 'deleted':
                lines.append(f"Property '{path}' was removed")
            case 'nested':
                lines.append(plain(item["children"], path_string=f'{path}.'))
                continue
            case 'plain':
                lines.append(f"Property '{path}' was updated. From "
                             f"{stringify_value(item['old_value'])} to "
                             f"{stringify_value(item['new_value'])}")
    return '\n'.join(lines)


def stringify_value(item):
    if isinstance(item, dict):
        return '[complex value]'
    elif isinstance(item, (bool, type(None))):
        return bool_lower(item)
    elif isinstance(item, (int, float)):
        return item
    else:
        return f"'{item}'"
