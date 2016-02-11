#!/usr/bin/env python

import yaml
import json
import pprint

with open("capitals.yaml", "r") as f_yaml:
    capitals = yaml.load(f_yaml)
print "====== YAML file ======"
pprint.pprint(capitals)

with open("capitals.json", "r") as f_json:
    capitals = json.load(f_json)
print "====== json file ======"
pprint.pprint(capitals)

