# Merge given two lists into one sorted list

# Solution : 1

a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]
c = []
while a and b:
    if a[0] < b[0]:
        c.append(a.pop(0))
    else:
        c.append(b.pop(0))
        
# either a or b can be not empty
print(c + a + b)


# Solution : 2 in pythonic way

a.extend(b)
c = sorted(a)
print(c)
