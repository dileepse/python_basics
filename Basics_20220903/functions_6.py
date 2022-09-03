# Function with arguments and with return type
# Declaration/Definition - one time 
def addition(a,b):
    c = a + b # 100 + 200
    return c

def check_odd_even(xyz): # result = 400
    if xyz % 2 == 0:
        print("Given number ",xyz,"is Even")
    else:
        print("Given number ",xyz,"is Odd")

result = addition(101011,300)
print("Addition result is : ", result)

check_odd_even(result)