#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cfg_file = CiscoConfParse("cisco_ipsec.txt")

crypto_maps = cfg_file.find_objects(r"^crypto map CRYPTO")

for crypto_map in crypto_maps:
    print crypto_map.text
    for child in crypto_map.all_children:
        print child.text
