# Will raise error due to third parameter missing 
# a default value, since a default value was assigned 
# to the preceding positional parameter.

def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)