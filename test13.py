# -*- coding=utf-8 -*-

def trim(str):
    if(str==''):
        return str
    elif (str[0]!=' ')and(str[-1]!=' '):
        return str
    elif str[0]==' ':
        return trim(str[1:])
    else :
        return trim(str[0:-1])

def trim1(s):
    length = len(s)
    if length > 0:
        for i in range(length):
            if s[i] != ' ':
                break
        j = length - 1
        while s[j] == ' ' and j >= i:
            j -= 1
        s = s[i:j+1]
    return s

def trim2(s):  
    if s[:1] != ' ' and s[-1:] != ' ':  
        return s  
    elif s[:1] == ' ':  
        return trim(s[1:])  
    else:  
        return trim(s[:-1])  
        
# 测试:
if trim('hello  ') != 'hello':
    print 111111111111111111
    print('测试失败!')
elif trim('  hello') != 'hello':
    print 2222222222222222
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print 3333333333333333
    print('测试失败!') 
elif trim('  hello   world   ') != 'hello world':
    print 33333333334444444444
    print('测试失败!')
elif trim('') != '':
    print 444444444444444444
    print('测试失败!')
elif trim('    ') != '':
    print 5555555555555555555
    print('测试失败!')
else:
    print('测试成功!')
