import sys
import subprocess

#Verify Ip address is rechable
def ip_rechable(list):

    for ip in list:
        ip = ip.rstrip('\n')

        ping_reply = subprocess.call('ping %s -n 2' % (ip,), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if ping_reply == 0:
            print("\n* IP address {} is rechable".format(ip))
            continue

        else:
            print("\n* IP address {} is not rechable".format(ip))
            sys.exit()
