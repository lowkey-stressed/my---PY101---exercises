
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0]

]

for lists in my_list:
    for number in lists:
        if number % 2 == 0:
            print(number)