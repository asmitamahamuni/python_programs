def isAnagram(w1, w2):
  return sorted(w1) == sorted(w2)

words = [("evil","vile"), ("pat","tap"),("mile","nile")]
for w in words:
  print(w, isAnagram(w[0],w[1]))  
