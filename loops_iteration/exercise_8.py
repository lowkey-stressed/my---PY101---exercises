
# { key: value for element in iterable if condition }

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_dict = {f'{names}: {len(names)}'
           for names in my_set
           if len(names) % 2 != 0}

           
print(my_dict)