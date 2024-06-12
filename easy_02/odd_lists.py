
def oddities(lst):
    # counter = 1
    # length = len(lst)
    # new_lst = []

    # while counter < length + 1:
    #     if counter % 2 != 0:
    #       new_lst.append(lst[counter - 1])

    #     counter += 1
    
    # print(new_lst)

    return lst[0:len(lst):2]


    

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  
print(oddities([1, 2, 3, 4]) == [1, 3])        
print(oddities(["abc", "def"]) == ['abc'])     
print(oddities([123]) == [123])                
print(oddities([]) == [])                      