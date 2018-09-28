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
