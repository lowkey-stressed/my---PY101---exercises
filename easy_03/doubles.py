
def twice(n):
    string = str(n)
    half_len = int(len(string)/2)
    full_len = int(len(string))
    left_str = string[0:half_len]
    right_str = string[half_len:full_len]

    if left_str == right_str:
        return n
    else:
        return n*2



print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # Truec
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
