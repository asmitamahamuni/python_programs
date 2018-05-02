def reverse_words(message):
   reverse = message[::-1]
   words = reverse.split()
   r_words = []
   for w in words:
      r_words.append(w[::-1])
   return ' '.join(r_words)
   
def reverse_words2(message):
   words = message.split()
   words_rev = words[::-1]
   return ' '.join(words_rev)

def reverse_words3(message):
   return ' '.join([m[::-1] for m in message[::-1].split()])
   
def reverse_words4(message):
   return ' '.join(reversed(message.split()))
   
if __name__ == "__main__":
   message = "I like to think the moon is there even if I am not looking at it - Einstein"
   print("In = ", message)
   print("Out = ", reverse_words(message))
