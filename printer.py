def print_progress(line):
	title = 'About to execute command: ' + line.strip()
	top_bar = '           '

	for z in range(0, len(title), 1):
		top_bar += '_'
	print top_bar

	curr_cmd = '__________|About to execute command: ' + line.strip() + '|__________'
	print curr_cmd

	empty_line = '|'
	for y in range(0, len(curr_cmd) - 1, 1):
		empty_line += ' '
	empty_line += '|'
	print empty_line

	return curr_cmd


def print_cmd_completion_status(curr_cmd, output):
	success_string = '| command status: successful'
	invalid_string = '| command status: invalid/incomplete'
	if 'Invalid input' in output or 'Incomplete command' in output:
		for u in range(0, len(curr_cmd) - len(invalid_string), 1):
			invalid_string += ' '
		invalid_string += '|'
		print invalid_string
	else:
		for u in range(0, len(curr_cmd) - len(success_string), 1):
			success_string += ' '
		success_string += '|'
		print success_string

	end_line = '|'
	for x in range(0, len(curr_cmd) - 1, 1):
		end_line += '_'
	end_line += '|\n\n\n'
	print end_line