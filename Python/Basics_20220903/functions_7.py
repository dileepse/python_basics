# With argument and without return type
def check_odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

# When no return type is mentioned by default it returns None
result = check_odd_even(101)
print(result)
