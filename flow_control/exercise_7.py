
def number_range(number):
    if number < 0:
        return(f'{number} is less than 0.')
    elif not(number) and number <=50:
        return (f'{number} is between 0 and 50.')
    elif number >=51 and number <=100:
        return (f'{number} is between 51 and 100.')
    else:
        return (f'{number} is between 51 and 100.')


print(number_range(0))
print(number_range(25))
print(number_range(51))
print(number_range(75))
print(number_range(101))
print(number_range(-1))