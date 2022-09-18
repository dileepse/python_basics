

"""
list_append(lst, append_ele)

list_clear(lst)

list_count()

list_extend
"""

def list_append(lst, append_ele):
    lst = lst + [append_ele]
    return lst

def list_clear(lst):
    return []

def list_count(lst, ele_to_search):
    """
        step1 : Iterate over the list
        step2 : compare each element(temp) in the list with the ele_to_search
        step3 : if list element(temp) and ele_to_search matches then increment the count
    """
    count = 0
    for temp in lst:
        if temp == ele_to_search :
            count = count + 1
    return count
        
def list_extend(old_lst, new_list):
    """
        step1 : 
        step2 : 
        step3 : 
        old_lst = old_lst + new_list
        return old_lst
        for temp in new_list:
            old_lst = old_lst.list_append(temp)
        return old_lst
    """
    for temp in new_list:
        old_lst = old_lst + [temp]
    return old_lst

def list_index(lst, search_ele):
    """
        step1 : Iterate over the list using list
        step2 : compare each element(temp) from the iteration with search ele
        step3 : return element index if matches, if not return -1
    """
    index = -1
    not_found = -1
    for temp in lst: # [10,30,60,20,50,50,50]
        index = index + 1  # increment
        if temp == search_ele:
            return index
    return not_found

def list_insert_without_swap(lst,index,element_to_insert ):
    """
        lst[5] = lst[4] # lst[5] = 50

        lst[4] = lst[3]# lst[4] = 40

        lst[3] = lst[2] # lst[3] = 3

        lst[2] = 300
    """
    lst = lst + [None] # len = 6 so upto, index 5

    for temp in range(len(lst)-1,index,-1): # 5,4,3  index = 2
        lst[temp] = lst[temp-1]
    # 10, 20, 30, 30, 40, 50
    lst[index] = element_to_insert
    return lst

def list_insert_with_swap(lst,index,element_to_insert ): # [10,20,30,40,50]
    """
        lst = lst + [None] # [10,20,30,40,50, None]
        
        temp = lst[5] # temp = None
        lst[5] = lst[4] # lst[5] = 50
        lst[4] = temp # lst[4] = None
        
        # [10,20,30,40,None, 50]
        
        temp = lst[4] # temp = None
        lst[4] = lst[3] # lst[4] = 40
        lst[3] = temp # lst[3] = None
        
        # [10,20,30,None,40, 50]
        
        temp = lst[3]
        lst[3] = lst[2]
        lst[2] = temp
        
        # [10,20,None,30,40, 50]
    """
     # len = 6 so upto, index 5
    if index < len(lst):
        lst = lst + [None]
        print(lst)
        for temp in range(len(lst)-1,index,-1): # range(5,2,-1) 5,4,3
            swap_value = lst[temp] # temp = None
            lst[temp] = lst[temp-1] # lst[5] = 50
            lst[temp-1] = swap_value 
            print(lst)
            
        lst[index] = element_to_insert
        return lst
    else:
        lst = lst + [element_to_insert]
        return lst
        
# list_insert_with_swap(lst,index,element_to_insert )

lst = list_insert_with_swap([10,20,30,40,50,60,70,80],0,100 )
print(lst)




    



















    
# abc = [10,30,60,20,50,50,50]

#result = list_index(abc, 100)

#print(result)

# abc = [10,30,60,20,50,50,50]
# xyz = [1,2,3,4,5]

# abc = list_extend(abc,xyz)
# print(abc) # [10,30,60,20,50,50,50, 1,2,3,4,5]


#result = list_count(abc, 100)
#print(result)






#lst = list_append(lst, 100)
#abc = list_clear(abc)
