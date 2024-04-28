
set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.pop()
set1.add(range(5, 10))
print(set2)                     # this whatever set1 with the 
                                # additional range element added on
                                # line 5. Set1 and Set2 are referencing
                                # the same object thus Set2 will reflect
                                # the mutation from line 4.

