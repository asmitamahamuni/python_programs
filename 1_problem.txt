# Merging overlapped range

l = [(4,9), (20, 22), (1, 3), (24, 32), (23, 31), (40,50), (12, 15), (8,13)]
l = sorted(l)
print(l)

lnew = []
st = l[0][0]
end = l[0][1]

for item in l[1:]:
    if end >= item[0]:
        if end < item[1]:
            end = item[1]
    else:
        lnew.append((st,end))
        st = item[0]
        end = item[1]
    
lnew.append((st,end))

print(lnew)
