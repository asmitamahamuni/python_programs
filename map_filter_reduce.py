# Example of map reduce and filter :

integers = [ x for x in range(11)]
filter_data = list(filter(lambda x: x % 2 == 0, integers))
print(filter_data)
# output : [0, 2, 4, 6, 8, 10]

map_data = list(map(lambda x: x**2, integers))
print(map_data)
# output : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

from functools import reduce
reduce_data = reduce(lambda x, y: x + y, integers)
print(reduce_data)
# output : 55
