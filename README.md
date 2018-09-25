# Network-Automation
Generic SSH script to execute CLI commands on any device that can be accessed over SSH. But networking devices is the priority of this project

# Instalation

# Usage
## Log in Credentials
First you must make a file called "login credentials.txt". In this file you will include the IP address, username, and password on one line for one device. If you wish to write down devices but use them later you can "comment" them output by including a "#" as the first character in the line.
 
 Example: ```10.10.210.125 myusername mypassword```
 
 ## Writing commands to be executed
 Next, We need to configure the commands you want to run on the device(s). To do this,
we have multiple options:

1. Different configuration files for each device
