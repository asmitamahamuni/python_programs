def isCommonChild(st1,st2):
    
    # construct new strings from the input, only with common characters
    common1 = ''.join([c for c in st1 if c in st2])
    common2 = ''.join([c for c in st2 if c in st1])
    
    # no common chars, then just return with []
    if not common1 or not common2:
        return common1
    
    # O(n^2)
    # try every substring (with initial order of chars) of common1 
    # if it's a substring of common2. 
    # If it is, construct list of substrings
    subcommon = []
    mx = 0
    for i in range(len(common1)):
        j = i
        while (j < len(common1)):
            sub = common1[i:j+1]
            if sub in common2:
                subcommon.append(sub)
            j += 1
    print('subcommon=',subcommon)    
    # find the longes substring, and return it.
    mxsub = max(subcommon, key=len) 
    return mxsub
      
mystr = [('ABCD','ABDC'), ('HARRY','SALLY'),('AA','BB'),('SHINCHAN','NOHARAAA'),('ABCDEF','FBDAMN')]

for st in mystr:
    print(st)
    ret = isCommonChild(st[0],st[1])
    print(ret, len(ret))
    print()
