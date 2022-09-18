
"""
Functions :

len()

min()

max()

sum()

"""
# length output : 19



def get_list_length(lst):
    cnt = 0
    for temp in lst:
        cnt = cnt + 1
    return cnt


lst = [300,23,24,34,32,42,43,5,6,2,3]    

def get_min_ele(lst):
    if get_list_length(lst) == 0:
        return "Empty"
    elif get_list_length(lst) == 1:
        return lst[0]
    else:
        min_value = lst[0]
        for temp in range(1,get_list_length(lst)): # range(1,10) => 1,2,3,4,5,5,6,7,8,9
            if lst[temp] < min_value: # 5 < 23:
                min_value = lst[temp]
        return min_value

def get_max_ele(lst):
    if get_list_length(lst) == 0:
        return "Empty"
    elif get_list_length(lst) == 1:
        return lst[0]
    else:
        max_value = lst[0]
        for temp in range(1,get_list_length(lst)): # range(1,10) => 1,2,3,4,5,5,6,7,8,9
            if lst[temp] > max_value: # 5 < 23:
                max_value = lst[temp]
        return max_value

def get_lst_sum(lst):
    sum_value = 0
    for temp in lst:
        # print("sum_value = {sum_value} + {temp}".format(sum_value = sum_value, temp = temp))
        sum_value = sum_value + temp
    return sum_value



           
lst = [300,23,24,34,32,42,43,5,6,2,3]
lst = [200,3]
# result = get_max_ele(lst)
# print(result)
    
result = get_lst_sum(lst)
print(result)
    
# result = get_min_ele(lst)
# print(result)  



# lst_len = get_list_length(abc)
#print(lst_len)

