import json
from pathlib import Path

import yaml


def get_json(file_path):
    return json.load(open(file_path))


def get_yaml(file_path):
    return yaml.load(open(file_path), Loader=yaml.FullLoader)


def parse(file):
    return get_json(file) if Path(file).suffix == 'json' else get_yaml(file)