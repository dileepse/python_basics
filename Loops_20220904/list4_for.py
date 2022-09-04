# creating a list
"""
for <temp variable> in <iterable>:
    statement1
    statement2
    statement3

iterable 
    - range
    - list

"""
lst1 = [10,20,'Python',40,50,60]

for ele in lst1 : # iterable value [10,20,30,40,50,60]
    print(type(ele),ele)
    
"""
step 1 : check for iterable and compute and have it ready # [10,20,30,40,50,60]
step 2 : temp_variable nothing but ele will be assigned with 10
step 3 : execute the stements under for loop, in our case it is print
step 4 : temp_variable nothing but ele will be assigned with 20
step 5 : execute the stements under for loop, in our case it is print
step 6 : temp_variable nothing but ele will be assigned with 30
step 7 : execute the stements under for loop, in our case it is print
"""