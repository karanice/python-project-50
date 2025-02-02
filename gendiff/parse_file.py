import json
from pathlib import Path

import yaml


def get_json(file_path):
    return json.load(open(file_path))


def get_yaml(file_path):
    return yaml.load(open(file_path), Loader=yaml.FullLoader)


def parse(file_path):
    return get_json(file_path) if Path(file_path).suffix == 'json' else get_yaml(file_path)