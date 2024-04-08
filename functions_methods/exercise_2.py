
# This code will print 'bar' since foo is assigned 
# a value of 'bar' inside of the global scope.

foo = 'bar'
def set_foo():
    foo = 'qux'

set_foo()
print(foo)
