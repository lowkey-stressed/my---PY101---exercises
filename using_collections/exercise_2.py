# Use slicing to write Python code to print a 6-character substring of 'Launch
#  School' that begins with the first c.

text = 'Launch School'
# print(text[4:10])
start = text.find('c')
print(text[start:start+6])