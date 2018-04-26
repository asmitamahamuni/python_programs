import copy

class Foo(object):

  def __init__(self,value):
    self.value = value
    
  def __repr__(self):
    return str(self.value)

foo = Foo(1)

a = ['foo', foo]
b = a
c = a[:]
d = list(a)
e = copy.copy(a)
f = copy.deepcopy(a)

# Now we copied the original object.
# Let's modified the original,
# and see how it affects the copied object.

a.append('bar')
foo.value = 999

print('contents of objects')
print('original : %r\n assign : %r\n slice : %r\n'
      'list : %r\n  copy : %r\n deepcopy: %r\n'
      % (a,b,c,d,e,f))

print('Is it the same object as a-object?')
print('assign : %r\n slice : %r\n'
      'list : %r\n  copy : %r\n deepcopy: %r\n'
      % (id(b)==id(a), id(c)==id(a), id(d)==id(a),
         id(e)==id(a), id(f)==id(a)))
