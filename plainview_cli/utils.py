import json

def pretty_print_json(json_object):
    return json.dumps(json_object, sort_keys=True, indent=2, separators=(',', ': '))