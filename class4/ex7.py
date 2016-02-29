#!/usr/bin/env python

# Use Netmiko to enter into configuration mode on pynet-rtr2

from netmiko import ConnectHandler

def main():
    pynet2 = {
        'device_type': 'cisco_ios',
        'ip' : '50.76.53.27',
        'username' : 'pyclass',
        'port' : 8022,
        'password' : '88newclass'
    }

    pynet_rtr2 = ConnectHandler(**pynet2)
    pynet_rtr2.config_mode() 
    if pynet_rtr2.check_config_mode():
        print "We're in config mode"
        pynet_rtr2.send_command("logging buffered 33333")
    else:
        print "Nope, We're  NOT in config mode"

if __name__ == '__main__':
    main()
