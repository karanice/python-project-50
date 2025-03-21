from gendiff.styles.json import json
from gendiff.styles.plain import plain
from gendiff.styles.stylish import stylish


def format_diff(diff, format):
    match format:
        case 'stylish':
            return stylish(diff)
        case 'plain':
            return plain(diff)
        case 'json':
            return json(diff)
        

__all__ = (
    format_diff
)