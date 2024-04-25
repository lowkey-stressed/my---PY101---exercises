# Explain why the code below prints different values on lines 3 and 4.


text = "It's probably pining for the fjords!"
print(text[20:35])

# print(text[21:35].rfind('f'))     # 8
# print(text.rfind('f', 21, 35))    # 29

# Original Answer: 
# The reason these print different values is because slicing the text in line 3 creates
# a shallow copy of the original text that only includes 8 characters instead
# of 35. Line 4 is just returning the original index of f which is 29. 

