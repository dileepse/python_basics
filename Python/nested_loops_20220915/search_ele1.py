
# WAP search if Adi replica is available

walking_track = ['Rakesh','Rizwan', 'Jyoshna','Aziz', 'Chandu']

search_ele = 'Adi'

search_flag = False
for temp in walking_track: # ['Rakesh','Rizwan', 'Jyoshna','Aziz', 'Adi','Chandu' ]
    if temp == search_ele : # Rizwan == Adi  False
        search_flag = True
        break
# print(temp)

if search_flag == True :
    print("Found similar face to {search_ele}".format(search_ele = search_ele))
else:
    print("No Similar Face found to {search_ele}".format(search_ele = search_ele))
