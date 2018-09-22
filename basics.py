import paramiko


#First connect to the device
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.0.0.1',port=22, username='Router1', password='cisco')

#Now we can execute commands
stdin, stdout, stderr = ssh.exec_command('show ip int brief')
output = stdout.readlines()

#print the output to my screen
print '\n'.join(output)