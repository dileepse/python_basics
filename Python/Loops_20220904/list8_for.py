# WAP to find length of given list without using pre-defined function len()

"""
eg : list_length = len(lst)
len - predefined function
    how many arguments - 1
        possible argument - list/string
    what does it return - length of the given list(nothing but a number or integer)
    
for <temp_variable> in <iterable>:
    statement1
    statement2
    
Possible Iterables -
    range
    list

check_list_len(lst) return length 
"""


def check_list_len(lst):
    for ele in lst: # [10,20,30,40,50,60] 
        length = 0
        length = length + 1
    print("Overall length of the given list",length)

lst1 = [10,20,30,40,50,60] 
check_list_len(lst1)