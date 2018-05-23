# -*- coding=utf-8 -*-

def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def add_end(l=None):
    if l is None:
        l = []
    l.append('end')
    return l

def calc(nums):
    sum = 0
    for n in nums:
        sum = sum + n*n
    return sum
def calc1(*nums):
    sum = 0
    for n in nums:
        sum = sum + n*n
    return sum

def person(name, age, **kw):
    print("name:", name, "age:", age, "other:", kw)

def product(*args):
    sum = 1
    print args
    if args == ():
        raise TypeError
    for arg in args:
        sum = sum*arg
    return sum

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
