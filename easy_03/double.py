
def crunch(string):
    last_char = ''
    result = ''

    for char in string:
        if last_char != char:
            last_char = char
            result += char
        
    
    return result

  

    

print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')