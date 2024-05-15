
# Inputs: string_1, string_2
# Calculations: length of string1, length of string2
# Output: concatenation of shorter + long + shorter


def short_long_short(string1,string2):
    length1 = len(string1)
    length2 = len(string2)
    new_string = ''

    if length1 > length2:
        new_string = string2 + string1 + string2
    else:
        new_string = string1 + string2 + string1

    return new_string

print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")

      
