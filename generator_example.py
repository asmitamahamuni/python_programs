
def take(count, iterable):
  counter = 0
  for i in iterable:
    if counter == count:
      return
    counter += 1
    yield i
 
def run_take():
  iterable = [2,4,5,6,7,8,9]
  for item in take(3, iterable):
      print(item)


if __name__ == '__main__':
  run_take()
