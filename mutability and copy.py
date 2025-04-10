# 1. shallow copy
#    copies each element of a list
#    BUT remember: the element might be a pointer/reference/mutable

numbers.copy()


import copy

# 2. deepcopy
#    copies each element of a list recursively
#    THAT MEANS: if an element is a pointer/reference/mutable
#     then it will be also deepcopied

copy.deepcopy(numbers)

# 3. Be careful !

t1 =(1,2)
#t2 = (1,2)
t2 = t1
print(id(t1))
print(id(t2))


my_list = [3,6,9,4,6,711,88]

print(sorted(my_list)[-1])
print(my_list)