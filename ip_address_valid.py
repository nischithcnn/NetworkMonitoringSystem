import sys

# Checking the IP address
def ip_address_valid(list):

    for ip in list:
        ip = ip.rstrip('\n')
        ip_octate = ip.split('.')

        if ((len(ip_octate) == 4) and (1 <= int(ip_octate[0]) <=223) and (int(ip_octate[0]) != 169)
                and (int(ip_octate[0]) != 254) and
                (int(ip_octate[0]) != 127) and  (0 <= int(ip_octate[1]) <= 254)
                and (0 <= int(ip_octate[2]) <= 254) and (0 <= int(ip_octate[3]) <= 254) ):
            print("\n* Ip address {} is valid".format(ip))
            continue

        else:
            print("\n* IP address {} is invalid".format(ip))
            sys.exit()
