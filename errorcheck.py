# used for running os commands
import pexpect
import time

def error_check(device_brand, output_files_list):

    print '\n\n            Checking for errors\n'

    # Check for errors or invalid input
    for z in range(0, len(output_files_list), 1):
        title = output_files_list[z].strip('output-')
        title = title.strip('.txt')

        print ' ', z+1, ') Device ' + title
        # Palo alto key word is "Unknown command:"
        # Arista and Cisco key word is: "Invalid"
        cmd = 'cat ' + output_files_list[z] + ' | grep -B 2 Invalid'
        # print cmd
        process = pexpect.spawn('/bin/bash')
        process.sendline(cmd)

        if 'None' in str(process.before):
            print '\n      No Errors!'
        else:
            print process.before
        # process.interact()
        print '\n\n'