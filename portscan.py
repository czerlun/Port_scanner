#!/bin/python3

import socket
import sys
from datetime import datetime

if len(sys.argv) != 4:
    print("Use: ./portscan.py <ip_adress> start stop (range of scan port)")
    print("for example ./portscan.py 123.123.123.123 50 80")
    sys.exit(1)
else:
    target = socket.gethostbyname(sys.argv[1])

start = int(sys.argv[2])
stop = int(sys.argv[3])

print("-" * 50)
print("Scanning target "+ target)
print("Time started: "+ str(datetime.now()))
print("-" * 50)

try:
    for port in range(start,stop):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open ".format(port))
        else:
            print("Port {} is close ".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExit program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()    
