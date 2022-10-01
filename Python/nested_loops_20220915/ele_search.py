

# WAP to find if a given elemnt is available in the given list

# OGL -> TPTY => OGL,SKONDA, KAVALI, NELLORE, NPETA, RENIGUNTA, TPTY

number_to_search = 200

lst1 = [10,20,30,40,50,60,70,80,90]

search_flag = False

for value in lst1: # [10,20,30,40,50,60,70,80,90]
    if number_to_search == value: # 50 == 50
        search_flag = True
        break

if search_flag is True :
    print("The number you are searching is available ", number_to_search)
else:
    print("The number you are searching is not available ", number_to_search)
    