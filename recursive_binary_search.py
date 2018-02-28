# Recursive binary search

# returns True if found the item
# otherwise, returns False
def bSearch(a, item):
   if len(a) == 0:
      return False
   mid = len(a)/2
   if a[mid] == item:
      return True
   else:
      if a[mid] < item:
         return bSearch(a[mid+1:], item)
      else:
         return bSearch(a[:mid], item)

if __name__ =="__main__":
   a = [1,3,4,5,8,9,17,22,36,40]
   print(bSearch(a, 9))
   print(bSearch(a, 10))
   print(bSearch(a, 36))
   
