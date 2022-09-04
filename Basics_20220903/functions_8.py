# WAP to find greatest number among the given 3 arguments

def print_bigger_number(a,b,c):
    if a == b and a == c :
        print("A, B, C are equal")
    elif a > b and a > c :
        print("A is Bigger")
    elif b > c :
        print("B is bigger")
    else :
        print("C is bigger")


print_bigger_number(10,10, 10)