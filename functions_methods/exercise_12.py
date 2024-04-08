# Will raise error due to first parameter not having a default value
# and invoking foo with no argument on line 9

def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()