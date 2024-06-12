
def triangle(n):
    counter = 1

    while counter < n+1:
      print(spaces(n-counter) + stars(counter))
      counter += 1

def spaces(n):
      return (' ' * (n))

  

def stars(n):
    if n:
      return ('*' * n)
    else:
      return ('*' * (n + 1))



triangle(9)