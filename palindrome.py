import itertools

def isPalindrome(w):
   for i in range((len(w)+1)/2):
      if w[i] != w[-i-1]:
         return False
   return True

def isPalindrome_new(w):
   return w == w[::-1]
   
if __name__ == "__main__":
   word = "civic"
   for w in itertools.permutations(word):
      word = "".join(w)
      print("Is %s palindrome ? %s"  %(word, isPalindrome(word)))
