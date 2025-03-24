from gendiff.styles.to_json import to_json
from gendiff.styles.to_plain import to_plain
from gendiff.styles.to_stylish import to_stylish


def format_diff(diff, format):
    match format:
        case 'stylish':
            return to_stylish(diff)
        case 'plain':
            return to_plain(diff)
        case 'json':
            return to_json(diff)
        

__all__ = (
    format_diff
)