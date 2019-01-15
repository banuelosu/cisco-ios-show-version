import sys
import os
import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException

os.system('clear')

# First check if a file was passed to the script, quit if nothing was passed to script
try:
    input_file = sys.argv[1]
except:
    output = '''
You must pass a file with a device list to the script:
    
    "python3 main.py <path-to-file>"

Please try again.
'''
    print(output)
    exit()

# Check if the file can be opened, quit if it cannot be
try:
    with open(input_file, 'r') as f:
        device_list = f.read().splitlines()
except FileNotFoundError:
    print('\nThe file named: \'{}\' was not found. Please specify a different file and try again.\n'.format(input_file))
    exit()

# Credentials needed to authenticate to device
username = input('\nUsername: ')
password = getpass.getpass()

# Defining dictionary needed to connect to device
device_dictionary = {}
device_dictionary['device_type'] = 'cisco_ios'
device_dictionary['timeout'] = 10
device_dictionary['username'] = username
device_dictionary['password'] = password
device_dictionary['ip'] = None

# Print list of devices 
print('\nFound the following devices in the file:')
for device in device_list:
    print(' - ' + device)

# Verify it looks correct
while True:
    choice = input('\nPlease verify the information above looks correct. Would you like to continue? [Y|N]: ').upper().strip()

    if choice == 'Y':
        break
    elif choice == 'N':
        print('\nQuitting script...')
        exit()
    else:
        continue

failed_devices = []

# Loop through devices within device_list and run 'show version'
for device in device_list:
    device_dictionary['ip'] = device

    try:
        device_connector = ConnectHandler(**device_dictionary)
        print('Device: {}, Status: authenticated'.format(device))
    except (EOFError, SSHException, NetMikoTimeoutException, NetMikoAuthenticationException):
        # print('There appears to be an issue with authenticating onto: {}'.format(device))
        # Script will keep track of devices that it could not connect to
        failed_devices.append(device)
        continue
    
    command = 'show version'
    print('Device: {}, Command: {}'.format(device, command))
    print(device_connector.send_command(command))

# Print out list of devices that the script could not authenticate to
if len(failed_devices) > 0:
    print('\nThe script experienced an issue with the following devices: ')
    for device in failed_devices:
        print(' - ' + device)