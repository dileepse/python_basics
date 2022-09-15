
# WAP search if Adi replica is available

walking_track = ['Rakesh','Rizwan', 'Jyoshna','Aziz', 'Chandu']

search_list = ['Adi', "Chinna", "Chandu"]

# outer loop
for search_ele in search_list: # search_ele => Chandu
    search_flag = False
    # inner loop
    for temp in walking_track: # ['Rakesh','Rizwan', 'Jyoshna','Aziz', 'Chandu']
        if temp == search_ele : # Rizwan == Adi  False
            search_flag = True
            break
    # print(temp)
    if search_flag == True :
        print("Found similar face to {search_ele}".format(search_ele = search_ele))
    else:
        print("No Similar Face found to {search_ele}".format(search_ele = search_ele))
