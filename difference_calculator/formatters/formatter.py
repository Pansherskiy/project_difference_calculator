from difference_calculator.formatters.stylish import stylish
from difference_calculator.formatters.plain import plain


def formatter(diff, style):
    match style.lower():
        case 'stylish':
            return stylish(diff)
        case 'plain':
            return plain(diff)
        case _:
            print(f"Format '{style}' missing, choose among formats:"
                  f"\n'stylish'\n'plain'\n'json'")
