
# This also doesn't print anything because
# functions in python terminate when return 
# is called, so print(words) is never invoked.
def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')