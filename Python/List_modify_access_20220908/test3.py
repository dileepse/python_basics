lst1 = [10, 20, 300, 50, 20, 70, 40]

# print(lst1[x]) # 7 times , modify x

for x in range(len(lst1)): # range(len(lst1)) => range(7) => 0 to 6 , 7 not included
    if x == 5:
        print(lst1[x])