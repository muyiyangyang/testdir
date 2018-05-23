def search(l, x):
    length = len(l)
    m = length/2
    #print m
    while x in l:
      #yield x
      if x == l[m]:
        print m
        return l[m]
      elif x < l[m]:
        return search(l[:m], x)
      else:
        return search(l[m+1:],x)
    return -1

s = search([1,2,3,4,5,6],3)
print s
