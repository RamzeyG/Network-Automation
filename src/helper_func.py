


def check_kevin_file(k_file_name, kevin_flag, ip_commands, begin_found, start):
    if kevin_flag:
        print begin_found, start
        command_list = open(ip_commands, 'w')
        kevin_file = open(k_file_name, 'r')

        for line in kevin_file:
            while begin_found <= start:
                if line.startswith('######') and 'BEGIN CONFIG' in line:
                    begin_found += 1
                elif begin_found == start:
                    command_list.write(line.strip() + '\n')
                    print 'Writing the following cmd: [' + line.strip() + ']'

                line = kevin_file.next()
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
