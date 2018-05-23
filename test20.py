def search(l, x):
    length = len(l)
    low = 0
    while abs(low) < length:
        m = (length + low)/2
        #yield m
        if l[m] == x:
            return m
        elif l[m] > x:
            low = low - 1
        else:
            low = low + 1
    return -1

#for x in search([1,2,3,4,5,6,7], 7):
#    print x

def count(n):  
    print "cunting"  
    while n > 0:  
        print 'before yield'  
        yield n    
        n -= 1  
        print 'after yield'
#for x in count(4):
#    print x
