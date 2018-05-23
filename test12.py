# -*- coding=utf-8 -*-

def trim(s):
    length = len(s)
    if length != 0:
        if s[0] == ' ':
            return trim(s[1:])
        if s[-1] == ' ':
            return trim(s[:-1])
        
        for i in range(length-1):
            if s[i] == s[i+1] == ' ':
                return trim(s[0:i] + s[i+1:])
        #sl = s.split(' ')
        #while '' in sl:
        #    sl.remove('')
        #s = ' '.join(sl)

    return s
        
# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!') 
elif trim('  hello   world   ') != 'hello world':
    print('测试失败!')
elif trim('  hello   world   add  d') != 'hello world add d':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
