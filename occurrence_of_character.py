# Count occurrence of a character in a Python string

sentence='The Mississippi River'

# 1. Using list and map functions
def count_chars(s):
        s=s.lower()
        count=list(map(s.count,s))
        return (max(count))
        
print(count_chars(sentence))

# 2. Using list comprehension
def count_chars(s):
    s=s.lower()
    L = [s.count(c) for c in s]
    return max(L)
    
print(count_chars(sentence))

# 3. Using dict and fromkeys
sl = sentence.lower()

d = {}.fromkeys([x for x in sl],0)

for char in sl:
    d[char] += 1
    
print(d)

# 4. Using dict.get method
sl = sentence.lower()
d = {}
for c in sl:
    d[c] = d.get(c,0) + 1  
print d

# 5. Using dict comprehension
sentence = "The Mississippi River"
ans = dict((c,sentence.count(c)) for c in sentence)
print(ans)
