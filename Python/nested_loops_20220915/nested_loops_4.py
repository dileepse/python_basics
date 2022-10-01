
lst1 = []
for temp in range(1,4):
    lst1.append(temp)

lst2 = []
for temp in range(1,3):
    lst2.append(temp)
    

for temp1 in lst1: # 1 <- [1,2,3]
    for temp2 in lst2: # 1 <- [1,2]
        # print("{temp1} == {temp2}".format(temp1 = temp1, temp2 = temp2))
        if temp1 == temp2 :
            print("Hey Hello")