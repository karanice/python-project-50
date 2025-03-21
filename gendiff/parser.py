import json

import yaml


def parse(file, ext):
    match ext:
        case '.json':
            return json.load(open(file))
        case '.yml' | '.yaml':
            return yaml.load(open(file), Loader=yaml.FullLoader)
    