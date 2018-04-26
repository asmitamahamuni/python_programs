# iterative
def fibi(n):
   a, b = 0, 1
   for i in range(0,n):
     a, b = b, a+b
   return a

# recursive
def fibr(n):
   if n == 0: return 0
   if n == 1: return 1
   return fibr(n-2)+fibr(n-1)

for i in range(10):
   print (fibi(i), fibr(i))
   
   
def fib_generator(n):
   a, b = 0, 1
   for i in range(n):
      yield "({},{})".format(i,a)
      a, b = b, a+b

# loop through the generator
for item in fib_generator(10):
   print(item)
