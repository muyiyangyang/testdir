def search(l, x):
    length = len(l)
    low = 0
    if x in l:
      while low <= length:
        m = (length + low) / 2
        if l[m] == x:
            return m
        if l[m] < x:
            low = low + 1
        else:
            low = low - 1
    return -1

print search([1,2,3,4,6,7,8,11,12], 5)
print search([1,2], 2)
