
def multisum(number):
   lst = list(range(1,number+1))
   sum = 0
   for numbers in lst:
      if numbers % 3 == 0 or numbers % 5 == 0:
         sum += numbers
   return sum


print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)


