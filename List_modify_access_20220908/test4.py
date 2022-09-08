lst1 = [10, 20, 300, 50, 50, 70, 40]

"""
lst1[0] = 10
lst1[1] = 20
lst1[2] = 30
lst1[3] = 40
lst1[4] = 50
lst1[5] = 60
lst1[6] = 70
"""

value = 0
print(lst1)
for x in range(len(lst1)): # range(7) => [0,1,2,3,4,5,6]
    value = value + 10
    if lst1[x] != value: # 300 != 30
        lst1[x] = value
        print(lst1)

