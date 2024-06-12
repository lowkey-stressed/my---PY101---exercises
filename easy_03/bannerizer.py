




def print_in_box(string):

  str_len = len(string)

  if string:
    top_bottom(str_len)
    middle(str_len)
    print( '|' + string + '|')
    middle(str_len)
    top_bottom(str_len)
  else:
    top_bottom(str_len)
    print( ('|  |\n' * 3).strip())
    top_bottom(str_len)


def top_bottom(length):
    if length > 0:
        print('+' + multiply('-',length) + '+')
    else:
        print('+--+')



def middle(length):
     print('|' + multiply(' ',length) + '|')


def multiply(string, n):
    return string * n

       


print_in_box('To boldly go where no one has gone before.')
# print_in_box('')