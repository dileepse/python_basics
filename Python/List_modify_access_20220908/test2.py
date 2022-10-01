# Accessing list by index

"""
for <temp_variable> in <iterable>:
    statement1

iterable -
    range()
    list

print() - new line

print(lst1[0])
print(lst1[1])
print(lst1[2])
print(lst1[3])
print(lst1[4])
print(lst1[5])
print(lst1[6])
"""

lst1 = [10, 20, 300, 50, 20, 70, 40]

# print(lst1[x]) # 7 times , modify x

for x in range(len(lst1)): # range(len(lst1)) => range(7) => 0 to 6, 7 not included
    # print(x)
    print(lst1[x])
    
"""
step1 - Decode/compute iterable range(7) - 0,1,2,3,4,5,6

step2 - into x send 0

step3- execute print(lst1[x]) => print(lst1[0])

step4 - into x send 1

step5 - execute print(lst1[1]) => print(lst1[1])
"""
    




