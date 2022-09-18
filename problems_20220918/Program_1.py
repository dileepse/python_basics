
# WAP a program to add number 10 to all the elements in the list

lst = [1,2,3,4,5,6,7,8,9]

# output : [11,12,13,14,15,16,17,18,19]
new_lst = []
for temp in lst :
    new_lst.append(temp + 10)

print(new_lst)