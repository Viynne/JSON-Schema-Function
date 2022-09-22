import os
import json


# Define iterator
def run_iteration(dictionary_input: dict, files_input):
    # Loop through values and keys of the input dictionary
    for k, v in files_input.items():
        # Skip key having the name Attribute
        if k == 'attributes':
            continue
        dictionary_input[k] = {"type": str(type(v)),
                               "tag": "",
                               "description": "",
                               "required": False,
                               "properties": {}}
        for k1, v1 in v.items():
            dictionary_input[k]['properties'][k1] = {'type': str(type(v1)),
                                                     'tag': '',
                                                     'description': '',
                                                     'required': False,
                                                     'properties': {}}
            if type(v1) == dict:
                # Repeat iteration for values with Key Value Pair
                for k2, v2 in v1.items():
                    dictionary_input[k]['properties'][k1]['properties'][k2] = {'type': str(type(v2)),
                                                                               'tag': '',
                                                                               'description': '',
                                                                               'required': False,
                                                                               'properties': {}}
                    if type(v2) == dict:
                        for k3, v3 in v2.items():
                            dictionary_input[k]['properties'][k1]['properties'][k2]['properties'][k3] = {
                                'type': str(type(v3)),
                                'tag': '',
                                'description': '',
                                'required': False,
                                'properties': {}}
                            if type(v3) == dict:
                                for k4, v4 in v3.items():
                                    dictionary_input[k]['properties'][k1]['properties'][k2]['properties'][k3][
                                        'properties'][
                                        k4] = {
                                        'type': str(type(v4)),
                                        'tag': '',
                                        'description': '',
                                        'required': False,
                                        'properties': {}}


# Dump Dictionary into json file
def to_json(input_dictionary, file_path):
    with open(file_path, 'w') as js:
        json.dump(input_dictionary, js)
