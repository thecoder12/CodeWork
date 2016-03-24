__author__ = 'dw'

## client-server atchitecture
# Aim: create git clone on server.
# ways - ssh to server from client using paramiko.
        # then execute command on server.

        ## this code executes the command on the server, but it doesnt wait for the process to complete.
        # it seems like below code is useable for small tasks from commands like, ls -ltrh /tmp, or sudo dmesgs.
        # but when it comes to heavy lifting like, execute IO for 1gb on server on /tmp directory, in this case it might take
        # around 5mins+ time, to create 1gb file on server. such tasks doesnt seem to work, as the code doesnt wait for the task to complete so
        # script doesnt have any idea whether the task is completed or not.
        ##

import time
from threading import Thread

thread_list = list()

def git_clone(i, cmd):
    import paramiko
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(
        paramiko.AutoAddPolicy())
    ssh.connect('localhost', username='dw', password='root123')
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print stdin
    print stdout
    print stderr

for i in range(3):

    cmd = 'git clone "https://github.com/duckduckgo/zeroclickinfo-goodies" "/tmp/thecoder12_c' + str(i) + '"'
    cmd = 'cd /tmp;wget http://distro.ibiblio.org/puppylinux/puppy-4.1-k2.6.25.16-seamonkey.iso'
    print cmd

    t = Thread(target=git_clone, args=(i,cmd))
    t.start()
    thread_list.append(t)

print(len(thread_list))

for t in thread_list:
    if t.isAlive():
        t.join()

print ('All done...!!!!')