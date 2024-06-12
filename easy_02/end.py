
def penultimate(string):
    lst = string.split(' ')
    lst_length = len(lst)
    result = lst[lst_length - 2]
    return result


print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == 'is')