
def get_final_hostname(hostname, hostname_found, new_file):

    if '# ' in hostname:
        rm_prompt = hostname.split('#')
        hostname = rm_prompt[0]
        hostname_found = True
    elif '> ' in hostname:
        rm_prompt = hostname.split('>')
        hostname = rm_prompt[0]
        hostname_found = True
    elif '$ ' in hostname:
        rm_prompt = hostname.split('$')
        hostname = rm_prompt[0]
        hostname_found = True

    # Look for" hostname(currentmode)"
    if '(' in hostname:
        rm_parenthesis = hostname.split('(')
        hostname = rm_parenthesis[0]

    # Look for username@hostname
    if '@' in hostname:
        rm_user = hostname.split('@')
        hostname = rm_user[1]
        hostname = hostname.strip('~').strip(':').strip()

    # on linux machines: for "hostname:directory"
    elif ':' in hostname:
        rm_user = hostname.split(':')
        hostname = rm_user[0]
    if hostname_found:
        new_file += '-' + hostname + '.txt'
        result = open(new_file, 'w')
    if not hostname_found:
        print 'DID NOT FIND HOSTNAME, exiting program'
        exit()

    return new_file, result