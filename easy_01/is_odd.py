
def is_odd(integer):
    if abs(integer) % 2 != 0:
        return True
    else:
        return False


print(is_odd(8))    # False
print(is_odd(-8))   # False
print(is_odd(7))    # True
print(is_odd(-7))   # True
print(is_odd(0))    # False