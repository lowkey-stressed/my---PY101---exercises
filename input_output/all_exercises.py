# Example 1
# # def hello():
# #     print('Hello')
# #     return True

# # Example 2
# hello()  
# print(hello()) 

# Example 3
# # print('Hello','My friend','What is you doing', sep = '--------', end = '-------\n')

# Example 4
# # greeting = 'Salutations'

# # def well_howdy(who):
# #     greeting = 'Howdy'
# #     print(f'{greeting}, {who}')

# # well_howdy('Angie')
# # print(greeting)

# Example 5
def scope_test():
    if True:
        foo = 'Hello'
    else:
        bar = 'Goodbye'

    print(foo)
    print(bar)

scope_test()