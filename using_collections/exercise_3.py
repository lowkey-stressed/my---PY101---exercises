# Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple 
# should be in reverse order from the original. It should also exclude the 
# first and last members of the original. The result should be the 
# tuple (4, 3, 2).

# tuple1 = (1,2,3,4,5)
# list1 = list(tuple1)
# list1.reverse()
# # result = tuple(list1[1:4])

my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[3:0:-1]


print(result)