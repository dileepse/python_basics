
# WAP to find if a given elemnt is available in the given list

lst1 = [10,20,30,40,50,60,70,80,90]

number_to_search = 60

for value in lst1: # [10,20,30,40,50,60,70,80,90]
    if number_to_search == value: 
        print("The number you are searching is available ", number_to_search)
        break
    else:
        print("The number you are searching is not available ", number_to_search)
    