# -*- coding: utf-8 -*-
"""List_Methods.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rDD3IlKd4a9ko5ge0b5i0hkOI5enSM3H

List Methods - 

append()

clear()

copy()

count() - Returns the number of elements with the specified value

extend()

index() - Returns the index of the first element with the specified value

insert() - 	Adds an element at the specified position

pop() - Removes the element at the specified position

remove() - Removes the first item with the specified value

reverse() - 

sort() -
"""

"""
Methods
  Description : 
  Arguments :
  Return Value/Type : 
"""

lst1 = [1,2,3,4,5,6,7,8]

lst2 = [10,20,30,40,50,60,70]

names = ["Adi","Chandu"]

cities = ["Ongole", "Hyderabad","Tirupati"]

"""
Functions -
min()
max()
len()
sum()
"""

lst2 = [10,20,30,40,50,60,70]

print(min(lst2))

print(max(lst2))

print(len(lst2))

print(sum(lst2))

"""
Method Calling - variable =  object_name.methods_name(args if any)
Methods - append()
  Description : Adds the provided at the end of the list
  Arguments : any element which you want to add
  Return Value/Type : None
"""

lst1 = [1,2,3,4,5,6,7,8]

print(lst1)

lst1.append(10)
print(lst1)
print(min(lst1))

lst1 = [1,2,3,4,5,6,7,8]

lst1.append(10)

print(lst1)

"""
General Method Calling - variable(LHS) =  object_name.methods_name(args if any) (RHS)
Methods - clear()
  Description : Clears/Removes all the list elements 
  Arguments : No Arguments
  Return Value/Type : None
"""

lst1 = [1,2,3,4,5,6,7,8]

lst1.append(10)

print(lst1)

lst1.clear()

print(lst1)

"""
Deep Copy vs Shallow Copy
General Method Calling - variable(LHS) =  object_name.methods_name(args if any) (RHS)
Methods - copy() - It does a shallow
  Description : Used to copy the list contents into another list but with a different address/reference
  Arguments : No Arguments
  Return : Returns a shallow copy of the list
"""


lst1 = [1,2,3,4,5]

lst2 = lst1.copy()

lst2.append(6)

print(lst1, lst2)
print(id(lst1), id(lst2))

"""
General Method Calling - variable(LHS) =  object_name.methods_name(args if any) (RHS)
Methods - count()
  Description : Used to find the occurence of any element provided as arguments
  Arguments : any elements you want to search or find for its occurence
  Return Value/Type : integer value, i.e. no.of time given element present
"""

lst1 = [1, 2, 3, 4, 5, 6,2,3,2,3,2,3,2]

count_2 = lst1.count(2)

count_100 = lst1.count(100)

print(count_2, count_100)

"""
General Method Calling - variable(LHS) =  object_name.methods_name(args if any) (RHS)
Methods - extend()
  Description : Used to find the occurence of any element provided as arguments
  Arguments : any elements you want to search or find for its occurence
  Return Value/Type : integer value, i.e. no.of time given element present
"""
lst1 = [1, 2, 3, 4, 5]
lst2 = [10,20,30,40,50]

lst1.append(lst2) # [1, 2, 3, 4, 5, [10,20,30,40,50] ]

print(len(lst1))
print(lst1)

"""
General Method Calling - variable(LHS) =  object_name.methods_name(args if any) (RHS)
Methods - extend()
  Description : Appends the elements in the iterable passed to the calling object(list)
  Arguments : Iterable
  Return Value/Type : None
"""
lst1 = [1, 2, 3, 4, 5]
lst2 = [10,20,30,40,50]

lst1.extend("Adi") # [1, 2, 3, 4, 5, 10,20,30,40,50]

print(len(lst1))
print(lst1)

str1 = "Python"

for temp in str1:
  print(temp)

"""
index() - Returns the index of the first element with the specified value

General Method Calling - variable(LHS) =  object_name.methods_name(args if any) (RHS)
Methods - index()
  Description :  Returns the index of the first element with the specified value
  Arguments : element in the list for which you need index
  Return Value/Type : Index Number(Integer) if element available, Error if element not available

"""

lst1 = [10,20,30,40,50]

index_10 = lst1.index(10)

print(index_10)

lst1 = [10,20,30,40,50]

index_10 = lst1.index(100)

print(index_10)

lst1 = [20,30,40,50,20,30,10,10]

index_10 = lst1.index(10)

print(index_10)

"""
insert() - 	Adds an element at the specified position
General Method Calling - variable(LHS) =  object_name.methods_name(args if any) (RHS)
Methods - insert()
  Description :  Adds an element at the specified index
  Arguments : 2 arguments(index where we want to insert and element which we want to insert)
  Return Value/Type : None

"""

lst1 = [10,20,30,40,50,60]

lst1.insert(2,123)

print(lst1[2])

"""

General Method Calling - variable(LHS) =  object_name.methods_name(args if any) (RHS)
Methods - pop()
  Description :  Removes the element at the specified index
  Arguments : No Mandatory arguments Optionally ou can pass the index where you want to remove the element
  Return Value/Type : Returns the element which it removes(Can be an integer or string or any thing as it is)
"""
lst1 = [10,20,30,40,50,60]

ele = lst1.pop(2)

print(ele)

print(lst1)

lst1 = [10,20,30,40,50,60]

ele = lst1.pop()

print(ele)

print(lst1)

"""

General Method Calling - variable(LHS) =  object_name.methods_name(args if any) (RHS)
Methods - remove()
  Description :  Removes the first occurence with the specified value
  Arguments : Element you want to remove
  Return Value/Type : None if element available, if element not available returns ValueError
"""

lst1 = [10,20,30,40,50,60]

lst1.remove(40)

print(lst1)

lst1 = [10,20,30,40,50,60]

lst1.remove(400)

print(lst1)

"""

General Method Calling - variable(LHS) =  object_name.methods_name(args if any) (RHS)
Methods - reverse()
  Description :  Reverse the order of elements in the list
  Arguments : No Positional Arguments
  Return Value/Type : None
"""

lst1 = [10,20,30,40,50,60]

lst1.reverse()

print(lst1)

"""

General Method Calling - variable(LHS) =  object_name.methods_name(args if any) (RHS)
Methods - sort()
  Description :  Sort Elements in the list
  Arguments : No Positional/Mandatory Arguments Required
  Return Value/Type : None
"""

lst1 = [10,6,90,33,9999,45,76,38,44]

lst1.sort()

print(lst1)

lst1 = [10,6,90,33,9999,45,76,38,44]

lst1.sort(reverse=True)

print(lst1)

"""
Programming Aptitude
Functions
count()
extend()
index()
insert() 
pop()
remove()
reverse()
sort() - Will take

Class MyList -
  Functions
  count()
  extend()
  index()
  insert() 
  pop()
  remove()
  reverse()
  sort() 

1.] Problem Statement
2.] Logic - 10 mins/15 mins
3.] Code/Syntax Implementation
"""