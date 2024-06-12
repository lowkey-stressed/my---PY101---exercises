
def center_of(string):
    
    str_length = int(len(string))
    half_string = int(str_length/2)

    if str_length % 2 == 0:
        return string[half_string-1:half_string+1]
    else:
        return string[half_string]
    

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                 