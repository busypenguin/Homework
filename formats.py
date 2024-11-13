import yaml
import json


with open('people.json', 'r') as file:
    json_data = file.read()

data = json.loads(json_data)
yaml_data = yaml.dump(data, default_flow_style=False)
print(yaml_data)
