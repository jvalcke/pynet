#!/usr/bin/

import pygal
import time
from snmp_helper import snmp_get_oid_v3, snmp_extract

def get_snmp_v3_data(device, snmp_user, oid):
    """ returns SNMP data """
    return snmp_extract(snmp_get_oid_v3(device, snmp_user, oid))

def main():
    ip_addr = '50.76.53.27'
    port = 7961
    pynet_rtr1 = (ip_addr, port)
    a_user = 'pysnmp'
    auth_key = 'galileo1'
    encrypt_key = 'galileo1'
    snmp_user = (a_user, auth_key, encrypt_key)

    oids = {'ifInOctets' : '1.3.6.1.2.1.2.2.1.10.5',
            'ifInUcastPkts' : '1.3.6.1.2.1.2.2.1.11.5',
            'ifOutOctets' : '1.3.6.1.2.1.2.2.1.16.5',
            'ifOutUcastPkts' : '1.3.6.1.2.1.2.2.1.17.5'}

    data = {'ifInOctets' : [],
            'ifInUcastPkts' : [],
            'ifOutOctets' : [],
            'ifOutUcastPkts' : []}

    tprev = {'ifInOctets' : [],
             'ifInUcastPkts' : [],
             'ifOutOctets' : [],
             'ifOutUcastPkts' : []}

    for oid, num in oids.items():
	tprev[oid] = int(get_snmp_v3_data(pynet_rtr1, snmp_user, oid=num))

    for t in range(12):
        time.sleep(300)
        for oid, num in oids.items():
            delta = int(get_snmp_v3_data(pynet_rtr1, snmp_user, oid=num)) - int(tprev[oid])
            data[oid].append(delta)

    print"{}".format(data)
            
    line_chart = pygal.Line()
    line_chart.title = 'Input/Output Packets'
    line_chart.x_labels = range (5,65,5)

    line_chart.add('InPackets', data['ifInUcastPkts'])
    line_chart.add('OutPackets', data['ifOutUcastPkts'])
    line_chart.render_to_file('packets.svg')

    line_chart = pygal.Line()
    line_chart.title = 'Input/Output Bytes'
    line_chart.x_labels = range (5,65,5)

    line_chart.add('InBytes', data['ifInUcastPkts'])
    line_chart.add('OutBytes', data['ifOutUcastPkts']) 
    line_chart.render_to_file('bytes.svg')

if __name__ == '__main__':
    main()
