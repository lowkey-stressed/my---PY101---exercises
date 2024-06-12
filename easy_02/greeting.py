
def greeting():
    name = input('What is your name? ')
    name_length = len(name)

    if name[name_length-1] == '!':
        print(f'hello {name}. why are we yelling? '.upper())
    else:
        print(f'Hello {name}.')


greeting()