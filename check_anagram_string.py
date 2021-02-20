def isAnagram(w1, w2):
  if sorted(w1) != sorted(w2):
    return False
  return True

words = [("evil","vile"), ("pat","tap"),("mile","nile")]
for w in words:
  print(w, isAnagram(w[0],w[1]))  
