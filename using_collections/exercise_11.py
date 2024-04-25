                                        # My Answers    # Correct Answers
print('johnson' in 'Joe Johnson')       # True          # False
print('sen' not in 'Joe Johnson')       # True          # True
print('Joe J' in 'Joe Johnson')         # False         # True
print(5 in range(5))                    # False         # False
print(5 in range(6))                    # True          # True
print(5 not in range(5, 10))            # False         # False
print(0 in range(10, 0, -1))            # False         # False
print(4 in {6, 5, 4, 3, 2, 1})          # True          # True
print({1, 2, 3} in {1, 2, 3})           # True          # False
print({3, 2} in {1, frozenset({2, 3})}) # false         # True