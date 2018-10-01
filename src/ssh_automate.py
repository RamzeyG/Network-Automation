import paramiko
import time
import argparse

# Remove bad chars
import re

# used for running os commands
import pexpect

# Import my helper functions
from printer import *
from errorcheck import *
from devicetype import *
from helper_func import *

#              ssh_automate.py
# This is a simple program that ssh's into Networking devices and
# gets the interface configuration. This program requires all devices'
# ssh information reside in the file "config.txt", which should be in the
# same directory as this script.
#
# This program assumes devices are already set up for ssh (instructions
# can be found in the file "sshSetupCisco.txt" for Cisco devices)


parser = argparse.ArgumentParser()
parser.add_argument('-kfile', '--kevinfile')
parser.add_argument('-sf', '--singlefile')
parser.add_argument('-b', '--devicebrand', default='cisco')

args = parser.parse_args()
kevin_file = args.kevinfile
single_file = args.singlefile
device_brand = args.devicebrand

# Check if device_brand is compatible with this program
check_device_brand_compatability(device_brand)

# Get config commands based off device brand
conf = config_mode.get(device_brand)

# kevin flag is off by default
kevin_flag = False

# create an ssh session
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def readFile(fileName):
	deviceList =[]
	numOfDevices = 0
	readfile = open(fileName, "r")
	for line in readfile:
		# Remove leading and trailing spaces
		line = line.strip()

		# Skip commented out and blank lines (\n) which have a len of 2
		if not line.startswith('#') and not line.startswith('//') and len(line) > 2:
			line = line.strip("\r\n")
			line = line.split(" ")
			deviceList.append([line[0], line[1], line[2]])
			numOfDevices += 1
	return numOfDevices, deviceList


# DEFUALT COMMANDS I NEED TO IMPLEMENT:
# enable, conf t, terminal len 0
def execute_commands(ip_commands, ssh_remote, device_name, kevin_flag, k_file_name):
	global begin_found
	global start

	begin_found, start = check_kevin_file(k_file_name, kevin_flag, ip_commands, begin_found, start)

	new_file = 'output-' + device_name

	# Write extra new line (fixes a lot of ouput issues)
	add_extra_line(ip_commands)

	# Start executing commands
	command_list = open(ip_commands, 'r')
	# # Executing config commands
	# config_cmds = conf.split('\n')
	# for f in range(0,len(config_cmds), 1):
	# 	curr_cmd = print_progress(config_cmds[f])
	# 	ssh_remote.send(config_cmds[f])
	# 	time.sleep(3)
	# 	output = ssh_remote.recv(655350)
	# 	print_cmd_completion_status(curr_cmd, output)

	first_run = 1
	# Initial sleep to wait for banner to come in
	time.sleep(3)
	# executing user commands
	for line in command_list:
		if 'show' in line:
			sleep_time = 5
		else:
			sleep_time = 1
		cmd = line.strip()
		if len(cmd) > 0 and '!' != cmd:
			curr_cmd = print_progress(line)
			# print 'cur cmd, len is ', curr_cmd, len(curr_cmd)
			# Now we can execute commands
			ssh_remote.send(line.lstrip())

			time.sleep(sleep_time)

			# Get ssh response.
			new_output, result, new_file = get_ssh_response(ssh_remote, first_run, new_file)
			if first_run:
				final_result = result
				first_run = False
			print_cmd_completion_status(curr_cmd, new_output)

			# Write output to the output file
			final_result.write(new_output)
	final_result.close()
	command_list.close()
	remove_extra_line(ip_commands)
	return new_file


# Main()

# Read in file for address, username and password
numOfDevices, deviceList = readFile("log-in-credentials.txt")


# Establish Global vars
global begin_found
global start
start = 1  # 1
begin_found = 0  # 0

# check if we have a kevin_file
if kevin_file:
	kevin_flag = True

# List of output file names
output_files_list = []


for i in range(numOfDevices):
	print "********** Now Going into device: ", deviceList[i][0], " ************"
	# print begin_found, start
	ssh.connect(deviceList[i][0], port=22, username=deviceList[i][1], password=deviceList[i][2], look_for_keys=False)

	ssh_remote = ssh.invoke_shell()

	if single_file:
		output_file = execute_commands(single_file, ssh_remote, deviceList[i][0], kevin_flag, kevin_file)
	else:
		output_file = execute_commands(deviceList[i][0], ssh_remote, deviceList[i][0], kevin_flag, kevin_file)
	
	ssh.close()

	begin_found += 1

	output_files_list.append(output_file)

error_check(device_brand, output_files_list)