



"""
result_sum = result_sum + 10 # result_sum = 10

result_sum = result_sum + 20 # result_sum = 30

result_sum = result_sum + 30 # 60

result_sum = result_sum + 40 # 100

result_sum = result_sum + 50 # 150

result_sum = result_sum + 60 # 210

"""

lst = [10,20,30,40,50,60] 
def get_list_sum(lst):
    result_sum = 0
    for ele in lst : # [10,20,30,40,50,60] 
        result_sum = result_sum + ele
    return result_sum

final_result = get_list_sum(lst)
print(final_result)