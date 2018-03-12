# Double the given value using decorator

def doubleIt(myfnc):
   def doubleItInside(*args):
     return myfnc(*args)*2
   return doubleItInside

@doubleIt
def oldFnc(n):
   return n*n

#oldFnc = doubleIt(oldFnc)

print(oldFnc(5))
