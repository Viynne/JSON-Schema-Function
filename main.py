import json
import os
from sniff_schema import run_iteration, to_json

# Define Filepaths
file_one = os.path.join('data', 'data_1.json')
file_two = os.path.join('data', 'data_2.json')

# Read contents of file into python dictionary
with open(file_one) as json_1:
    file_1 = json.load(json_1)

with open(file_two) as json_2:
    file_2 = json.load(json_2)

# Declare empty dictionary
dictionary = {}
dictionary_2 = {}

if __name__ == '__main__':
    # Function call for both files
    run_iteration(dictionary, file_1)
    run_iteration(dictionary_2, file_2)

    to_json(dictionary, os.path.join('schema', 'schema_1.json'))
    to_json(dictionary_2, os.path.join('schema', 'schema_2.json'))
