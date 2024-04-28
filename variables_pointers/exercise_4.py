
dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}


dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])       # My answer: [1, 2, 3]
                        # Answer: [1,42,3] because a shallow copy was created

