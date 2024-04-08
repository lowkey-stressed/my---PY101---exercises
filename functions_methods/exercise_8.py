# This code will also raise an error
# because we added too many arguments

def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)