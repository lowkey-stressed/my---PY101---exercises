
def xor(object1,object2):
    # if (object1 and not object2) or (not object1 and object2):
    #     return True
    # else:
    #     return False

    if object1 and not object2:
        return True
    elif not object1 and object2:
        return True
    else:
        return False
    


print(xor(5,0) == True)
print(xor(False,True) == True)
print(xor(1,1) == False)
print(xor(True,True) == False)