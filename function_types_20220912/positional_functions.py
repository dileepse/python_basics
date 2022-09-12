
# WAP which return sum of 3 digits
# Positional argument functions

def get_sum(a,b,c):
    print("Value of a is : {a_value}".format(a_value = a))
    print("Value of b is : {b_value}".format(b_value = b))
    print("Value of c is : {c_value}".format(c_value = c))
    result = a + b + c
    return result

sum_res = get_sum(100,20,30)
print(sum_res)