# Write program for usage of Map, reduce and filter

from functools import reduce

l = [x for x in range(10) if x % 2 == 0]
print(l)

m = list(filter(lambda x:x % 2 == 0, [x for x in range(10)] ))
print(m)

o = list(map(lambda x: x**2, m))
print(o)

p = reduce(lambda x,y:x+y, o)
print(p)
