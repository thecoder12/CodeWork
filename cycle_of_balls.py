'''
Problem statement:
You are given a Bucket with 100 balls, with 3 different colours(red, blue, green). 
You are asked to pick 10 balls from the bucket with a sequence of Red, Blue, Green.
So, here you need a chain of sequence till 10 balls are pulled.
'''

from itertools import *
j = 0
for i in cycle(['Red', 'Blue', 'Green']):
    print i
    j += 1
    if j > 10:
        break
