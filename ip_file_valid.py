import os.path
import sys

# Verify Ip address file and content validity
def ip_file_valid():

    #Prompting user for input
    input_file = input("\n# Enter the IP file path and name (e.g. C:\ip.txt)")

    #Checking if the file exist
    if os.path.isfile(input_file) == True:
        print("\n* IP File valid \n")
    else:
        print("\n* File {} doesnot exist \n".format(input_file))

    #Open the user file
    file_1 = open(input_file, 'r')
    file_1.seek(0)

    #Read teh content of file line by line
    ip_list = file_1.readlines()

    #Closing the file
    file_1.close()

    #Return the ip address list
    return ip_list
