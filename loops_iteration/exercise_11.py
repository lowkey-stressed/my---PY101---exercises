
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

# index = 0
# while index < len(my_list):
#     index_1 = 0
#     while index_1 < len(my_list[index]):
#         number = my_list[index][index_1]
#         if number % 2 == 0:
#             print(my_list[index][index_1])
#         index_1 += 1
    
#     index += 1

for lists in my_list:
    for number in lists:
        if number % 2 == 0:
            print(number)

# outer_index = 0
# while outer_index < len(my_list):
#     inner_index = 0
#     while inner_index < len(my_list[outer_index]):
#         number = my_list[outer_index][inner_index]
#         if number % 2 == 0:
#             print(number)

#         inner_index += 1

#     outer_index += 1