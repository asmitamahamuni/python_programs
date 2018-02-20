cities = {'San Francisco': 'US', 'London':'UK',
        'Manchester':'UK', 'Paris':'France',
        'Los Angeles':'US', 'Seoul':'Korea'}

# => {'US':['San Francisco', 'Los Angeles'], 'UK':[,], ...}

from collections import defaultdict
# using collections.defaultdict()
d1 = defaultdict(list) # initialize dict with list
for k,v in cities.items():
    d1[v].append(k)
print(d1)

# using dict.setdefault(key, default=None)
d2 = {}
for k,v in cities.items():
       d2.setdefault(v,[]).append(k)
print(d2)
