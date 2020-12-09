def isAnagram(w1, w2):
  if (sorted(list(w1)) != sorted(list(w2))):
    return False
  return True

words = [("evil","vile"), ("pat","tap"),("mile","nile")]
for w in words:
  print(w,isAnagram(w[0],w[1]))  
