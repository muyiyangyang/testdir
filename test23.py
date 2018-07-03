def ch_me(oldlist):
    print id(oldlist)
    newlist=oldlist
    print id(newlist)
    if len(newlist)>5:
        newlist=['a','b','c']
    for i,e in enumerate(newlist):
        if isinstance(e, list):
            newlist[i]='***'
    print newlist
    print id(newlist)
