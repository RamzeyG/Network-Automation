INSTRUCTINO TO USE ssh_automate.py


First you must make a file called "login credentials.txt". In this file you will
 include the IP address, username, and password on one line for one device.
 If you wish to write down devices but use them later you can "comment" them output
 by including a "#" as the first character in the line.
 
  EX: "10.10.210.125 myusername mypassword"
 
 As of now, DO NOT leave blank lines in the file. Those will be supported in a future 
 update.
 
Next, We need to configure the commands you want to run on the device(s). To do this,
we have multiple options:

 
1. Different config files for each device.

By default, the program assumes you are having one file per device. This file contains the configuration
commands you want to apply to this particualr device. the name of the file must be the IP address of the
device you want to apply commands to excluding commands like "conf t", "en", etc.

EX: file name: "10.33.66.42" (no extention) must contains all configuration commands.


Once this is done, simply run the program: "python ssh_automate.py"

The output of the terminal will be saved into a file with the ip addres an "-output" appended to this new file.


2. Using 1 config on multiple devices (opposite of option 1)

If you use the single file flag: "-sf <File Name>" you can spcify the single file that contains all the lines you want
to run on every device listed in your "log in credentials.txt" file.

3. Using 1 config file with different commands per device.

First make a config file that contains the config for each device seperated with the following sytax:

EX: "############# BEGIN CONFIGURATION FOR <hostname or IP> ###########"

The program looks for this line to seperate the commands.

This method requiers following a strct rule set. The order of devices in "login credentials.txt" must match the 
order of commands for each device in the config file. 

EX: 

login credentials.txt                                            configfile.txt

10.10.210.125 myusername mypassword                              ############# BEGIN CONFIGURATION FOR 10.10.210.125 ###########
10.20.210.124 myuser newPass                                     int fe1/0
                                                                 ip adr 10.10.210.128 255.255.255.0
																 ############# BEGIN CONFIGURATION FOR 10.20.210.124 ###########
																 vlan10
																 description myVlan10
