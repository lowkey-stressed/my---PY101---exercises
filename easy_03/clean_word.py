
def clean_up(string):

    new_string = ''
    previous = False
    
    for char in string:
        if not char.isalpha():
            if not previous:
              new_string += ' '
              previous = True
        else:
            new_string += char
            previous = False
            


    return new_string








 
  
 



print(clean_up("---what's my +*& line?") == " what s my line ")

  