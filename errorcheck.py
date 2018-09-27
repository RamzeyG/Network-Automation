# used for running os commands
import pexpect
import time
from devicetype import *

def error_check(device_brand, output_files_list):

    print '\n\n            Checking for errors\n'

    # Check for errors or invalid input
    for z in range(0, len(output_files_list), 1):
        title = output_files_list[z].strip('output-')
        title = title.strip('.txt')

        print ' ', z+1, ') Device ' + title

        # DELETE ME:
        if 'juniper' in device_brand:
            print 'ERROR: I DON"T HAVE THE RIGHT unknown cmd yet'
        cmd = 'cat ' + output_files_list[z] + ' | grep -B 2 ' +\
              invalid_cmd_key.get(device_brand)
        print cmd
        process = pexpect.spawn('/bin/bash')
        process.sendline(cmd)

        if 'None' in str(process.before):
            print '\n      No Errors!'
        else:
            print process.before
        # process.interact()
        print '\n\n'