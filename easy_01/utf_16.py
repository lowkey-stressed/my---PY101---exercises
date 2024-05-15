
def utf16_value(string):
    
    sum = 0

    for char in string:
        sum += ord(char)
    
    return sum


print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)
print(utf16_value("\u03A9") ==  937 )
