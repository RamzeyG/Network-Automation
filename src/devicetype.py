#     device_type.py
#
# This file contains the list of supported devices,
# and commands used by each device


# Commands to get into config mode
config_mode = {
		'cisco': 'en\nconf t\nterm len 0',
		'arista': 'en\nconf t\nterm len 0',
		'juniper': 'cli\nconfigure\nset cli screen-length 0',
		'pan': 'set cli pager off\nconfigure'
}



# keys used to look for "wrong command"
# Note, multi word keys need quotes around them
# aditional cmds: pan: Invalid syntax.
invalid_cmd_key = {
	'cisco': 'Invalid',
	'arista': 'Invalid',
	'juniper': '',
	'pan': '"Unknown command:"',
	'ubuntu': '"not found"'
}
