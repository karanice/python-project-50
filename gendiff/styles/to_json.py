from json import dumps


def to_json(diff):
    return dumps(diff, indent=4)