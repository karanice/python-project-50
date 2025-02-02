import json

def default_formatter(dict):
    return ((json.dumps(dict, indent=2)) .replace('"', '')).replace(',', '')
