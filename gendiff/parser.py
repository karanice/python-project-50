import json

import yaml


def parse(file, ext):
    match ext:
        case '.json':
            return json.load(open(file))
        case '.yml' | '.yaml':
            return yaml.safe_load(open(file))
        case _:
            raise ValueError("Недопустимое расширение файла")