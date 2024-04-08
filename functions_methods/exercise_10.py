# This code will print 42, 3.141592, 2)
# even though only two arguments are given,
# the third parameter was given a default value

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)