#Import the necessary modules
import sys
import time

from ssh_connection import ssh_connection
from ip_rechable import ip_rechable
from ssh_threadt import create_threads
from ip_address_valid import ip_address_valid
from ip_file_valid import ip_file_valid


# store the IP address in text file to list
ip_list = ip_file_valid()

#Check the validity of each IP address
try:
    ip_address_valid(ip_list)
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

#Check IP address are rechable
try:
    ip_rechable(ip_list)
except KeyboardInterrupt:
    print("\n\n* Program aborted by user. Exiting...\n")
    sys.exit()

#Call thread function for multiple SSH connection
while True:
    create_threads(ip_list, ssh_connection)
    time.sleep(10)