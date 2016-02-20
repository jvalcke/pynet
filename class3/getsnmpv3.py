#!/usr/bin/

from snmp_helper import snmp_get_oid_v3, snmp_extract

def get_snmp_v3_data(device, snmp_user, oid):
    """ returns SNMP data """
    return snmp_extract(snmp_get_oid_v3(device, snmp_user, oid))

def main():
    ip_addr = '50.76.53.27'
    port = 8061
    pynet_rtr2 = (ip_addr, port)
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)

    output = get_snmp_v3_data(pynet_rtr2, snmp_user, oid='1.3.6.1.2.1.1.5.0')
    print output

if __name__ == '__main__':
    main()
