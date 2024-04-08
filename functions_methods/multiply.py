def multiply(number1,number2):
    result = number1 * number2
    return result

# Original approach to asking for the input from user
## number1 = int(input('Enter the first number: '))
## number2 = int(input('Enter the second number: '))
## print(f'{number1} * {number2} = {multiply(number1,number2)}')

# Second approach after seeing launch school solution
# Using a function to ask users for input removes the duplication
# of coercing the string from input into int or float
# this approach also makes the print function more efficient

def get_number(prompt):
   answer = input(prompt)
   return float(answer)

number1 = get_number('Enter the first number: ')
number2 = get_number('Enter the second number: ')
product = multiply(number1,number2)

print(f'{number1} * {number2} = {product}')



