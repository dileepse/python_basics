
# WAP which return sum of 3 digits
# Default argument functions
# Thumb Rule - first we should give positional argument then default arguments

def get_sum(a,b,c = 100):
    print("Value of a is : {a_value}".format(a_value = a))
    print("Value of b is : {b_value}".format(b_value = b))
    print("Value of c is : {c_value}".format(c_value = c))
    result = a + b + c
    return result

# sum_res = get_sum(10,20,c = 200)
sum_res = get_sum(c = 200, a = 10,b = 20) # Error 
print(sum_res)