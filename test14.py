# -*- coding: utf-8 -*-

def findMinAndMax(L):
    length = len(L)
    if length == 0:
        return (None, None)
    elif length == 1:
        return (L[0], L[0])
    else:
        L.sort()
        return (L[0], L[-1])

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
