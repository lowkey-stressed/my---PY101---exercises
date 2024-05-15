
def sum_or_product():
    while True:
      number = input('Pleae enter a number greater than 0: ')
      if number.isdigit() == False:
          continue
      if int(number) > 0:
          break
    
    
    lst = list(range(1,int(number)+1))
    choice = input('Enter "s" to compute the sum, or "p" to compute the product. ')
   
    if choice == 's':
        sum = 0
        for numbers in lst:
            sum += numbers
        print(sum)
            
    
    if choice == 'p':
        product = 1
        for numbers in lst:
            product *= numbers
        print(product)

         
    
sum_or_product()

