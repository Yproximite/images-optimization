import json
import os

root_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

with open(os.path.join(root_path, 'config.json')) as config_file:
    config = json.load(config_file)
