
def negative(n):
    if n > 0:
      return 0 - n
    elif n <= 0:
      return n  


print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True