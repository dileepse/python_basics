"""
# WAP to find greatest number among the given 3 arguments

def get_bigger_number(a,b,c):
    if a == b and a == c :
        return a
    elif a > b and a > c :
        return a
    elif b > c :
        return b
    else :
        return c


big_value = get_bigger_number(10,10, 10)
print(big_value)
"""


# WAP to find greatest number among the given 3 arguments

def get_bigger_number(a,b,c):
    if a == b and a == c :
        print("All numbers are equal")
    elif a > b and a > c :
        return a
    elif b > c :
        return b
    else :
        return c


big_value = get_bigger_number(10,10, 10)
print(big_value)