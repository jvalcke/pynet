#!/usr/bin/env python

import yaml
import json

capitals = ["London", "Oslo", "Madrid", {"France":"Paris", "Germany":"Berlin", "Italy":"Rome"}]
with open("capitals.yaml", "w") as f_yaml:
    f_yaml.write(yaml.dump(capitals, default_flow_style=False))
with open("capitals.json", "w") as f_json:
    json.dump(capitals, f_json)

