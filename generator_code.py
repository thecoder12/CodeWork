__author__ = 'DarkWhite'


def countdown(n):
    while n > 0:
        yield n
        n -= 1

for x in countdown(10):
    print('T-minus', x)

