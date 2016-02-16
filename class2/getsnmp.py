#!/usr/bin/env python

from snmp_helper import snmp_get_oid, snmp_extract

def get_snmp_data(device, OID):
    """ returns SNMP data """
    return snmp_extract(snmp_get_oid(device, OID))

def main():
    IP_ADDR = '50.76.53.27'
    COMMUNITY_STRING = 'galileo'
    SYS_NAME_OID = '1.3.6.1.2.1.1.5.0'
    SYS_DESCR_OID = '1.3.6.1.2.1.1.1.0'

    pynet_rtr1 = (IP_ADDR, COMMUNITY_STRING, 7961)
    pynet_rtr2 = (IP_ADDR, COMMUNITY_STRING, 8061)

    devices = [pynet_rtr1, pynet_rtr2]
    for device in devices:
        print device
        output = get_snmp_data(device, SYS_NAME_OID)
        print output
        output = get_snmp_data(device, SYS_DESCR_OID)
        print output

if __name__ == '__main__':
    main()
