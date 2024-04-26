
# numbers = [1,2,3,4,5,6]

# [print(number) for number in numbers if number > 2]

squares = [number * number for number in range(5)]
print(squares)


squares = []
for number in range(5):
    square = number * number
    squares.append(square)

print(squares)


multiples_of_6 = [number for number in range(20)
                  if number % 6 ==0 ]

print(multiples_of_6)