import json
import os

file_one = os.path.join('data', 'data_1.json')
file_two = os.path.join('data', 'data_2.json')

with open(file_one) as json_1:
    file_1 = json.load(json_1)

with open(file_two) as json_2:
    file_2 = json.load(json_2)


# Define recursion
def recurse_over_dictionary(new_value, current):
    for k, v in new_value.items():
        current['properties'][k] = {'type': str(type(v)),
                                    'tag': '',
                                    'description': '',
                                    'required': False,
                                    'properties': {}}
        if type(v) == dict:
            current = current['properties'][k]
            return recurse_over_dictionary(v, current)
        else:
            current['properties'][k].pop('properties')


dictionary = {}
for k, v in file_1.items():
    if k == 'attributes':
        continue
    dictionary[k] = {'type': type(v),
                     'tag': '',
                     'description': '',
                     'required': False,
                     'properties': {}}
    recurse_over_dictionary(v, dictionary[k])

print(dictionary)
