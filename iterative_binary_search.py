
 # Iterative binary search

# returns True if found the item
# otherwise, returns False
def bSearch(a, item):
   st = 0
   end = len(a)-1
   mid = len(a)/2
   left = st
   right = end
   while True:
      # found
      if a[mid] == item:
         return True
      # upper
      elif a[mid] < item:
         left = mid + 1
      # lower
      else:
         right = mid - 1

      mid = (left+right)/2
      if mid < st or mid > end: break
      if left == right and a[mid] != item: break
   return False

if __name__ =="__main__":
   a = [1,3,4,5,8,9,17,22,36,40]
   print(bSearch(a, 9))
   print(bSearch(a, 10))
   print(bSearch(a, 36))
   print(bSearch(a, 5))
   print(bSearch(a, 22))
