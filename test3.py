#!/usr/bin/python
# Filename: func_local.py

def func(x):
    print 'x is', x
    x = 2
    print 'Changed local x to', x

x = 50
func(x)
print 'x is still', x

print '111111111111\n'
def func1(y):
    #global x
    global x, y

    print 'y is', y
    print 'x is', x
    x = 2
    print 'Changed local x to', x

x = 50
func1(x)
print 'Value of x is', x
