#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

cfg_file = CiscoConfParse("cisco_ipsec.txt")

crypto_maps_g2 = cfg_file.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"set transform-set AES-SHA")

for crypto_map in crypto_maps_g2:
    print crypto_map.text
