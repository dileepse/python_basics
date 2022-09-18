# WAP a program to add number 10 to all the elements in the list
# Note don't take a new list
# output : [11,12,13,14,15,16,17,18,19]



def add_some_number(lst):
    for x in range(len(lst)):
        lst[x] = lst[x] + 10
    return lst

abc = [1,2,3,4,5,6]
new_lst = add_some_number(abc)

print(new_lst)


"""
Alogorithm => Step by Step procedure of solving a problem
    1.] We can modify any list using index
        lst[index] = desired_value
    2.] Loops
            Pattern
                lst[x] = lst[x] + 10
        
        
        lst[0] = lst[0] + 10

        lst[1] = lst[1] + 10

        lst[2] = lst[2] + 10

        lst[3] = lst[3] + 10

        lst[4] = lst[4] + 10

        lst[5] = lst[5] + 10
    
"""