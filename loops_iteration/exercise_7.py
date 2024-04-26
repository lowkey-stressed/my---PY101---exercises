
my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

# def find_integers(tuple):               # My original solution
#     list = []
#     for element in (tuple):
#         if type(element) is int:
#           list.append(element)c
#         else:
#            continue
#     return list

def find_integers(things):
    return [element
            for element in things
            if type(element) is int]

integers = find_integers(my_tuple)
print(integers)