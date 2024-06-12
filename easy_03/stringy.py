
def stringy(n):
    counter = 1
    result = ''

    while counter < n + 1:
        if counter % 2 != 0:
            result += '1'
            counter += 1
        else:
            result += '0'
            counter += 1
    return result


print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
      