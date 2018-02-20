ss = """I figured it out
I figured it out from black and white
Seconds and hours
Maybe they had to take some time"""

# Solution 1
words = ss.split()
d = {}.fromkeys(words,0)
for w in words:
    d[w] += 1
print(d)

# Solution 2
d = {}
for w in ss.split():
    d[w] = d.get(w,0) + 1
print(d)


# Solution 3 
from collections import defaultdict
d = defaultdict(int)
for w in words:
    d[w] += 1
print(d)



