import subprocess

__author__ = 'dw'

from subprocess import call
import shlex

import time
from threading import Thread

thread_list = list()

def git_clone(i, cmd):
    args = shlex.split(cmd)
    #s = subprocess.Popen(args, shell=True)
    s = subprocess.call(cmd, shell=True)
    #s.communicate()



for i in range(3):

    cmd = 'git clone "https://github.com/duckduckgo/zeroclickinfo-goodies" "/tmp/thecoder12_b' + str(i) + '"'
    cmd = 'cd /tmp;wget http://distro.ibiblio.org/puppylinux/puppy-4.1-k2.6.25.16-seamonkey.iso'
    print cmd

    t = Thread(target=git_clone, args=(i,cmd))
    t.start()
    thread_list.append(t)

print(len(thread_list))

for t in thread_list:
    if t.isAlive():
        t.join()

print 'All done...'