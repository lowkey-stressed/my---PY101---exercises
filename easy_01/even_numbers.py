
lst = list(range(1,100))

# Solution 1
# even_numbers = [number for number in lst if number % 2 == 0]

# Solution 2
new_lst = []
for number in lst:
    if number % 2 == 0:
        new_lst.append(number)


#print(even_numbers)

print(new_lst)