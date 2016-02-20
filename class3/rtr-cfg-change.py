#!/usr/bin/

import pickle
import os.path
from email_helper import send_mail
from snmp_helper import snmp_get_oid_v3, snmp_extract

def get_snmp_v3_data(device, snmp_user, oid):
    """ returns SNMP data """
    return snmp_extract(snmp_get_oid_v3(device, snmp_user, oid))

FILE = "timestamps"

def main():
    ip_addr = '50.76.53.27'
    port = 8061
    pynet_rtr2 = (ip_addr, port)
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)

    oids = {'sysUptime' : '1.3.6.1.2.1.1.3.0',
            'ccmHistoryRunningLastChanged' : '1.3.6.1.4.1.9.9.43.1.1.1.0',
            'ccmHistoryRunningLastSaved' : '1.3.6.1.4.1.9.9.43.1.1.2.0',
            'ccmHistoryStartupLastChanged' : '1.3.6.1.4.1.9.9.43.1.1.3.0'}

    change_times = {}
    for oid, num in oids.items():
        output = get_snmp_v3_data(pynet_rtr2, snmp_user, oid=num)
        change_times[oid] = output

    # get the old timestamps 
    old_change_times = {}
    if os.path.exists(FILE):
        f = open(FILE, "r")
        old_change_times = pickle.load(f)
        f.close()
    else:
        for oid in oids.keys():
            old_change_times[oid] = change_times[oid] 

    if int(old_change_times['ccmHistoryRunningLastChanged']) < int(change_times['ccmHistoryRunningLastChanged']):
        print "Running config has changed"
        send_mail("jeroen@valcke.com", "config changes", "config has changed", "jeroen@valcke.com")
    else:
        print "Running config has NOT changed"

    # save latest timestamps as a reference
    f = open(FILE, "w")
    pickle.dump(change_times, f)
    f.close()

if __name__ == '__main__':
    main()
