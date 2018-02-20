def isPrime(n):
   if n == 1:
      return False
   for t in range(2,n):
      if n % t == 0:
         return False
   return True

def primes(n=1):
   while n < 100:
      # yields n instead of returns n
      if isPrime(n): yield n
      # next call it will increment n by 1
      n += 1
      
for n in primes():
   print(n)
   
   
