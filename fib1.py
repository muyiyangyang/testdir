def fib(n):
    #result = []
    a, b = 0, 1
    #while len(result) < n:
    while a < n:
        #if b > 6:
        #    return
        #result.append(b)
        yield b
        a, b = b, a + b
    #return result

print fib(10)
for i in fib(10):
    print i
