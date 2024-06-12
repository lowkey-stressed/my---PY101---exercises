
def repeat(string, n):
    return ((string + '\n') * n).rstrip()

print(repeat('Hello',10))