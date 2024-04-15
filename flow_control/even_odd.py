# Solution 1 (Original)
#def even_or_odd(number):
#    if number % 2 == 0:
#        print('This number is even')
#    else:
#        print('This number is odd')

#Solution 2
def even_or_odd(number):
    print('This number is even' if number % 2 else 'This number is odd')


def user_input(prompt):
    return int(prompt)


entry = input('Enter an even or odd number: ')
even_or_odd(user_input(entry))
