#!/usr/bin/env python

# Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2

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
    time.sleep(1)
    remote_conn.send('configure terminal\n')
    time.sleep(1)
    remote_conn.send('logging buffered 21212\n')
    time.sleep(1)
    remote_conn.send('show run | inc "logging buffered"\n')
    output = remote_conn.recv(65535)
    print output

if __name__ == '__main__':
    main()
