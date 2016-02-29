#!/usr/bin/env python

# Use PExpect to change the logging buffer size (logging buffered <size>) on pynet-rtr2

import pexpect
import sys

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    port = 8022
    password = '88newclass'
    ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    #ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 5
    ssh_conn.expect('assword:')
    ssh_conn.sendline(password) 
    ssh_conn.expect('#')
    ssh_conn.sendline('configure terminal') 
    ssh_conn.expect('#')
    ssh_conn.sendline('logging buffered 20001') 
    ssh_conn.expect('#')
    ssh_conn.sendline('exit') 
    print ssh_conn.before

if __name__ == '__main__':
    main()
