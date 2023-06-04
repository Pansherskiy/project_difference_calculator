from difference_calculator.formatters.stylish import stylish


def formatter(diff, style):
    match style:
        case 'stylish':
            return stylish(diff)
