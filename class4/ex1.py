#!/usr/bin/env python

# Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2. 

import paramiko
import time

def main():
    ip_addr = '50.76.53.27'
    username = 'pyclass'
    port = 8022
    password = '88newclass'
    pre_remote_conn = paramiko.SSHClient()
    pre_remote_conn.load_system_host_keys()
    pre_remote_conn.connect(ip_addr,
                            username=username,
                            password=password,
                            port=port,
                            look_for_keys=False,
                            allow_agent=False)
    remote_conn = pre_remote_conn.invoke_shell()
    remote_conn.send('terminal length 0\n')
    remote_conn.send('show version\n')
    time.sleep(1)
    output = remote_conn.recv(65535)
    print output

if __name__ == '__main__':
    main()
