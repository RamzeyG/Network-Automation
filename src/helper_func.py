
from filename import *

#        get_ssh_response()
#
# Gets the response form the remote device
def get_ssh_response(ssh_remote, first_run, new_file):
    rcv_timeout = 6
    interval_length = 1
    hostname_found = False
    new_output = ''

    # Continue to read from buffer until output is done
    while True:
        if ssh_remote.recv_ready():
            output = ssh_remote.recv(1024)
            # # Remove unwanted chars
            # for x in output:
            # 	new_output += (re.compile(r'\x1b[^m]*m')).sub('', x)
            new_output += output

        # If recv buffer is empty (we got all the output)
        else:
            rcv_timeout -= interval_length

        if rcv_timeout < 0:
            if first_run:
                hostname = ''
                temp = new_output.split('\n')
                itterator = len(temp) - 1

                hostname = temp[itterator]
                # while itterator >= 0 and len(hostname) == 0:
                # 	# Otherwise, hostname is the last line in the output
                # 	hostname = temp[itterator]
                # 	itterator -= 1

                # Grab new file name, and append to file name (result)
                new_file, result = get_final_hostname(hostname, hostname_found, new_file)
            else:
                result = 'temp'
            break

    return new_output, result, new_file



#              check_kevin_file()
#
# This function determines if we are using a kevin file, and if so it will
# parse and separate the kevin file by each device.
#
# @param: k_file_name - name of the kevin file
# @param: kevin_flag - flag indicating if we have a kevin file
# @param: ip_commands - name of file we write commands to for "this" particular device
# @param: begin_found -
# @param:
def check_kevin_file(k_file_name, kevin_flag, ip_commands, begin_found, start):
    if kevin_flag:
        print 'KEVIN FLAG IS HERE'
        print begin_found, start
        command_list = open(ip_commands, 'w')
        kevin_file = open(k_file_name, 'r')
        # kevin_flag.seek(0, 2)  # go to end of file
        # eof = kevin_file.tell()  # get end-of-file position
        # kevin_file.seek(0, 0)  # go back to start of file
        for line in kevin_file:
            while begin_found <= start:
                if line.startswith('######') and 'BEGIN CONFIG' in line:
                    begin_found += 1
                elif begin_found == start:
                    command_list.write(line.strip() + '\n')
                    # print 'Writing the following cmd: [' + line.strip() + ']'

                # line = kevin_file.next()
                line = next(kevin_file)
                # break at end of file
                if line == '':
                    print 'BREAKING'
                    break
        command_list.close()
        start += 1
        begin_found = -1
        kevin_file.close()
        # print 'I AM EXITING', begin_found, start
        # exit()
    return begin_found, start



#      add_extra_line()
#
# This function adds an extra line to a file. This is needed
# in order to get the proper output of the last command
#
# @pram: file - file that a new line is appended to
def add_extra_line(file):
    command_list = open(file, 'a+')
    command_list.write('\n')
    command_list.close()




#      remove_extra_line()
#
# This function remove the extra line that was added by
# add_extra_line()
#
# @param: file - file used to remove extra line from
def remove_extra_line(file):
    # Open file and get the last line
    command_list = open(file, 'r')
    lines = command_list.readlines()
    last = lines[-1]
    command_list.close()

    # Remove the last line
    command_list = open(file, 'w')
    command_list.writelines([item for item in lines[:-1]])

    # Write the last line without a \n
    command_list.write(last.rstrip())
    command_list.close()
