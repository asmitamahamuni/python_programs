# Using subprocess module

import subprocess

class interfaces:
   def __init__(self):
      self.intf = []
      proc = subprocess.Popen(['ip', 'link', 'show'], stdout=subprocess.PIPE)
      line_count = 0
      while True:
         line = proc.stdout.readline()
         if line != '':
            if line_count % 2 == 0:
               self.intf.append(line)
         else:
            break
         line_count += 1
      self.counter = -1
      self.max = len(self.intf)

   def __iter__(self):
      return self

   def next(self):
      if self.counter >= self.max-1:
         raise StopIteration
      self.counter += 1
      return self.intf[self.counter]

f = interfaces()
for i in f:
   print(i)
