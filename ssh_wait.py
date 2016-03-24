__author__ = 'dw'

## client-server atchitecture
# Aim: create git clone on server.
# ways - ssh to server from client using paramiko.
        # then execute command on server.
        # wait till all the threads are completed/terminated
        #The below code is very good for doing heavy lifting tasks, like
        # wget iso file of 1gb from internet.
        # git clone a repo from internet.
        # in such cases the code/script waits for the process to complete.


import time
from threading import Thread

thread_list = list()

def git_clone(i, cmd):

    from paramiko import SSHClient, AutoAddPolicy
    import time
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect('127.0.0.1', username='dw', password='root123')
    sleeptime = 0.001
    outdata, errdata = '', ''
    ssh_transp = ssh.get_transport()
    chan = ssh_transp.open_session()
    # chan.settimeout(3 * 60 * 60)
    chan.setblocking(0)
    chan.exec_command(cmd)
    while True:  # monitoring process
        # Reading from output streams
        while chan.recv_ready():
            outdata += chan.recv(1000)
        while chan.recv_stderr_ready():
            errdata += chan.recv_stderr(1000)
        if chan.exit_status_ready():  # If completed
            break
        time.sleep(sleeptime)
    retcode = chan.recv_exit_status()
    ssh_transp.close()

    print(outdata)
    print(errdata)

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