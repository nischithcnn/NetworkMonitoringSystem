import paramiko
import os.path
import time
import sys
import re

# Checking the password file
user_file = input("\n# Enter the password file path and name (e.g. C:\pwd.txt)")

if (os.path.isfile(user_file)) == True:
    print("\n* Password file {} exists".format(user_file))

else:
    print("\n* Password file {} is not valid".format(user_file))
    sys.exit()

#Checking the Commands file
commands_file = input("\n# Enter the commands file path and name (e.g. C:\comands.txt)")

if (os.path.isfile(commands_file)) == True:
    print("\n* Password file {} exists".format(commands_file))

else:
    print("\n* Password file {} is not valid".format(commands_file))
    sys.exit()

# Connect to the device with SSH
def ssh_connection(ip):

    global user_file
    global commands_file

    try:
        selected_user_file = open(user_file, 'r')
        user_data = selected_user_file.readlines()
        user_list = user_data[0].split(',')

        #Reading user name and password from the file
        user_name = user_list[0].rstrip('\n')
        user_password = user_list[1].rstrip('\n')

        selected_user_file.close()

        #Create a SSH session
        session = paramiko.SSHClient()

        #Accept the host keys
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        #Connect to the host device with username and password
        session.connect(ip.rstrip('\n'), username = user_name, password = user_password )

        # Start an interactive shell session on the router
        connection = session.invoke_shell()

        # Setting terminal length for entire output - disable pagination
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        # Entering global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        # Open user selected file for reading
        selected_cmd_file = open(commands_file, 'r')

        # Starting from the beginning of the file
        selected_cmd_file.seek(0)

        # Writing each line in the file to the device
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)

        # Closing the user file
        selected_user_file.close()

        # Closing the command file
        selected_cmd_file.close()

        # Checking command output for IOS syntax errors
        router_output = connection.recv(65535)

        if re.search(b"% Invalid input", router_output):
            print("* There was at least one IOS syntax error on device {} :(".format(ip))

        else:
            print("\nDONE for device {} :)\n".format(ip))

        # Test for reading command output
        print(str(router_output) + "\n")

        #Extract cpu utilization value from the device
        cpu = re.search(b"%Cpu\(s\):(\s)+(.+?)(\s)+us",router_output)
        utilization = cpu.group(2).decode('utf-8')

        with open("C:\\Users\\nisch\\cpu.txt",'a') as f:
            f.write(utilization + '\n')

        #device_int_config = re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",str(router_output))
        #print(device_int_config)

        # Closing the connection
        session.close()

    except paramiko.AuthenticationException:
        print(
            "* Invalid username or password :( \n* Please check the username/password file or the device configuration.")
        print("* Closing program... Bye!")
