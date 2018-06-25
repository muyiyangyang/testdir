def print_prime2(n):
    for i in xrange(2, n):
        print 'i: %d' % i
        for j in xrange(2, i):
            print 'j: %d' % j
            if i % j == 0:
                break
        else:
            print '%d is a prime number.' % i

print_prime2(10)
