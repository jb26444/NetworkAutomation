import paramiko
import time
import getpass
import os

configuration = open("commands.txt").readlines()
network_devices = open("ip.txt").readlines()

UN = raw_input("Username : ")
PW = getpass.getpass("Password : ")

# This For loop calls host list in the seed file "ip.txt"
for ip in network_devices:
  try:
    print ip
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=22, username=UN, password=PW)
    remote = ssh.invoke_shell()
    remote.send('term len 0\n')
    time.sleep(1)
# This for loop uses config file 'host_config1.py' to enter commands one by one
    for command in configuration:
        remote.send(' %s \n' % command)
        time.sleep(2)
        buf = remote.recv(65000)
        print buf
        file = open(ip, 'a')
        file.write(buf)
        file.close()
    ssh.close()
  except:
    pass
