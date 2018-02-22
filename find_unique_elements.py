# Making a list with unique element from a list with duplicate elements

dup_list = [1,2,3,4,4,4,5,1,2,7,8,8,10]
unique_list = list(set(dup_list))
print(unique_list)

# output : [1, 2, 3, 4, 5, 7, 8, 10]
