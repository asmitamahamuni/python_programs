#print cube of each element from the list

# using map
def cubic(x):
	return x*x*x

items = [x for x in range(11) if x % 2 == 0]
new_list = list(map(cubic, items))
print(new_list)

# output : [0, 8, 64, 216, 512, 1000]

# using lambda function
new_list = list(map(lambda x,y: x*y, [1,2,3], [4,5,6]))
print(new_list)
# output : [4, 10, 18]
