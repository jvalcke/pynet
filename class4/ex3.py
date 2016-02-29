#!/usr/bin/env python

# Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2

import pexpect
import sys

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    port = 8022
    password = '88newclass'
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    #ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 3
    ssh_conn.expect('assword:')
    ssh_conn.sendline(password) 
    ssh_conn.expect('#')
    ssh_conn.sendline('show ip int brief') 
    ssh_conn.expect('#')
    print ssh_conn.before

if __name__ == '__main__':
    main()
