# WAP to find average of given elements in the list
# sum and count 

def get_list_count(inp_lst): # inp_lst = lst
    """
    Description : This function is to find the length of list or string
    arguments :
        - lst : accepts list/string
    returns :
        - count of list as an integer
    """
    count = 0
    for ele in inp_lst: # [10,20,30,40,50,60] 
        count = count + 1
    return count

def get_list_sum(some_list): # some_list = lst
    """
    Description : This function is to find the sum of list elements
    arguments :
        - lst : accepts list/string
    returns :
        - sum of list as an integer
    """
    result_sum = 0
    for ele in some_list: 
        result_sum = result_sum + ele
    return result_sum
        
def get_average(pass_sum,  pass_cnt): # pass_sum = 210, pass_cnt = 6
    return pass_sum/pass_cnt # 210/6

lst = [10,20,30,40,50,60] 

count_res = get_list_count(lst)

sum_res = get_list_sum(lst) # 210

result_average = get_average(sum_res, count_res) 
# assignment operation(3 parts LHS, RHS,assignment)/function calling

print(result_average)

