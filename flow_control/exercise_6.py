def convert_upper(word):
    print(word.upper() if len(word)>= 10 else word)


user_input = input('Please enter a word: ')
convert_upper(user_input)


