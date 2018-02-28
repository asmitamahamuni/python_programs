# Find list of anagrams from a list of words

anagram = []
words = ['fired', 'alert', 'remain', 'alter', 'allergy', 'gallery',
         'abets', 'baste', 'fried', 'beast', 'beats']

words_dict = {}
for w in words:
   words_dict[w] = ''.join(sorted(w))

# make a list of groups with the same value
new_words = sorted(words_dict.values())

anagram = {}
for s in set(new_words):
   anagram[s]=[]
   for k,v in words_dict.items():
      if s == v:
         anagram[s].append(k) 
   
anagram_list = []
for k,v in anagram.items():
   anagram_list.append(v)
   
print(anagram_list)
