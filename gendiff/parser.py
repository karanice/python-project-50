import json
from os.path import splitext

import yaml


def parse(file_path):
    match splitext(file_path)[1]:
        case '.json':
            return json.load(open(file_path))
        case '.yml' | '.yaml':
            return yaml.load(open(file_path), Loader=yaml.FullLoader)
    