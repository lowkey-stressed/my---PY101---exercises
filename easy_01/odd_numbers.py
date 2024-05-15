
lst = list(range(1,100))

# Solution 1
# odd_numbers = [number for number in lst if number % 2 != 0]

# Solution 2
new_list = []
for number in lst:
    if number % 2 != 0:
        new_list.append(number)


print(new_list)