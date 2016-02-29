#!/usr/bin/env python

# Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx

from netmiko import ConnectHandler

def main():
    pynet1 = {
        'device_type': 'cisco_ios',
        'ip' : '50.76.53.27',
        'username' : 'pyclass',
        'port' : 22,
        'password' : '88newclass'
    }
    pynet2 = {
        'device_type': 'cisco_ios',
        'ip' : '50.76.53.27',
        'username' : 'pyclass',
        'port' : 8022,
        'password' : '88newclass'
    }
    srx = {
        'device_type': 'juniper',
        'ip' : '50.76.53.27',
        'username' : 'pyclass',
        'port' : 8022,
        'password' : '88newclass'
    }

    devices = [ pynet1, pynet2, srx ]

    for a_device in devices:
        a_device_conn = ConnectHandler(**a_device)
        output = a_device_conn.send_command("show arp")
        print output

if __name__ == '__main__':
    main()
