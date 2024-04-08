
# This code will throw an error because print(foo)
#  is calling a variable that is out of scope.
def set_foo():
    foo = 'bar'

set_foo()
print(foo)
