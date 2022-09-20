# python libraries imports
# python modules import

# class definition
# function definition
def list_count(lst, ele_to_search):
    """
        step1 : Iterate over the list
        step2 : compare each element(temp) in the list with the ele_to_search
        step3 : if list element(temp) and ele_to_search matches then increment the count
    """
    try:
        count = 0
        for temp in lst:
            if temp == ele_to_search :
                count = count + 1
        return count
    except Exception as e:
        print(str(e))

lst1 = [10,20,30,40,50,60]
result1 = list_count(lst1, 30)
print("lst1 related",result1)

if __name__ == "__main__":
    lst2 = [1,2,3,4,5]
    result2 = list_count(lst2, 30)
    print("lst2 related",result2)
    