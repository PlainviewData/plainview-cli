import os
import json
from jsonschema import validate
from jsonschema import ValidationError
from urllib.parse import urljoin

def is_valid(schema_name, object):
    '''Checks whether an object is valid given a schema_name'''
    schema = get_schema(schema_name)
    try:
        validate(object, schema)
    except ValidationError:
        return False
    return True
    
def get_schema(schema_name):
    print(os.getcwd())
    return json.loads(open(os.path.join(os.getcwd(), 'plainview_cli', 'schemas', schema_name + '.json')).read())