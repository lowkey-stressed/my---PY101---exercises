
def century(year):
  
    if year % 100 == 0:
        century = int(year/100)
    else:
        century = int(year/100) + 1 

    century_digits = century % 100
    century_str = str(century_digits)
    

    # return century_digits
  
    if century_digits < 10 or century_digits > 19:
        if int(century_str[len(century_str)-1]) == 1:
            return f'{century}' + 'st'
        elif int(century_str[len(century_str)-1]) == 2:
            return f'{century}' + 'nd'
        elif int(century_str[len(century_str)-1]) == 3:
            return f'{century}' + 'rd'
        else:
            return f'{century}' + 'th'
    else:
            return f'{century}' + 'th'
        
    return century


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
print(century(112013) == "1121st")        # True


    





