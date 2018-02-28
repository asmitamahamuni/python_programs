# How to count the number of instances

class A:
   total = 0

   def __init__(self, name):
     self.name = name
     A.total += 1

   def status():
      print("Total number of instance of A : ", A.total)
   status = staticmethod(status)


a1 = A("A1")
a2 = A("A2")
a3 = A("A3")
a4 = A("A4")

A.status()
