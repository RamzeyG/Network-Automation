# Network-Automation
Generic SSH script to execute CLI commands on any device that can be accessed over SSH. But networking devices is the priority of this project

# Instalation

# Usage
## Log in Credentials
First you must make a file called "login credentials.txt". In this file you will include the IP address, username, and password on one line for one device. If you wish to write down devices but use them later you can "comment" them output by including a "#" as the first character in the line.
 
 Example: 
 ```
 # This is a comment. Device sw-01's credentials is bellow:
 10.10.210.125 myusername mypassword
 ```
 
 ## Writing commands to be executed
 IMPORTANT: When making your commands, ensure to include an extra line with "!" at the end of the file. Otherwise you won't receive the proper output. A fix is currently being worked on.
 
 Next, We need to configure the commands you want to run on the device(s). To do this,
we have multiple options:

1. Different configuration files for each device (Default)

   By default, the program assumes you are having one file per device. This file contains the configuration commands you want to apply to this particualr device. The name of the file must be the IP address of the device you want to apply commands to (with no file extentions). Eventually I would like to allow the user to exclude commands like "conf t", "enable", "write mem", etc. but for now they need to be entered manually into the configuration file.
   
    Once this is done, simply run the program: ```python ssh_automate.py```
    The output of the terminal will be saved into a file with with the following name: ```<ip_address>-output-<device_host_name>.txt```

2. Using a single configuration file on multiple devices (opposite of option 1)
   
   If you would like to execute a single list of commands on all devices in "login credentials.txt" Then you want to use the single file flag ```-sf <file_name>``` to specify the single file you want to run on every device.
   
   Once this file is created run the program with the following syntax: ```python ssh_automate.py -sf <file_name>```
  
3. Using a single configuration file with different commands per device
 To use a single file with different commands per device a strict syntac needs to be followed. The file with your configuration must look like the following:
    ```
    ############# BEGIN CONFIGURATION FOR sw-tx-01 ###########
    !
    interface Ethernet66
    description MLAG to sw-2 Ethernet66
    speed forced 1000full
    channel-group 66 mode active
    !
    ############# BEGIN CONFIGURATION FOR sw-tx-02 ###########
    !
    interface Ethernet66
    description MLAG to sw-1 Ethernet66
    speed forced 1000full
    channel-group 66 mode active
    !
    ```
    IMPORTANT: Make sure you keep the log in credentials in the credentials file the same order as the device commands noted above. The 
 This file is called a kevin file. To run the program using this method, use the following syntax: ```python ssh_automate.py -kfile <file_name>```
 
 
