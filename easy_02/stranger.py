
def greetings(list, dictionary):
    string = ''
    role = ''

    for name in list:
        string += name + ' '
    
    
    
    for name in dictionary.values():
        role += name + ' '
    
    return 'Hello, ' + string.strip() + '!' + ' Nice to have a ' + role + 'around.'



greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},)

print(greeting)