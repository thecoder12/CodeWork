#!/usr/bin/python

import os

def convert2size(ss, count):
    i = 1
    while( i <= count ):
        ss = ss/1024
        i = i + 1
    return ss


def bytes2other( size, size_compare ):
    para = size_compare[-2:]
    s = ''
    size_compare = size_compare[:-2]
    
    ### kb onvert
    if para == 'kb' or para == 'Kb' or para == 'KB' or para == 'K':
        s = convert2size(int(float(size)),1)

    ## mb convert
    if para == 'mb' or para == 'Mb' or para == 'MB' or para == 'M':
        s = convert2size(int(float(size)),2)

    ## gb convert
    if para == 'gb' or para == 'Gb' or para == 'GB' or para == 'G':
        s = convert2size(int(float(size)),3)

    if s == int(float(size_compare)):
        print('SAME<>' + str(size_compare) + '<>' + str(s))
        return 0
    else:
        print('<not same>'+ str(size_compare) + '<>' + str(s))
        return 1

    
def getfilesize():
    size = os.path.getsize('/media/dw/Big Data/VID_20151109_072915482_cut.mp4')
    bytes2other(size, '727.7mb')

if __name__ == "__main__":
    #bytes2other('50','50k')
    getfilesize()
