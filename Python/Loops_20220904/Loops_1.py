# range() - It will be used with for loop
"""
for <temp_variable> in <iterable>:
    staement1
    staement2
    staement3
"""

for temp in range(3): # [0,1,2]
    print("I won't join lately")
"""
o/p :
I won't join lately
I won't join lately
I won't join lately
"""
for x in range(3): # [0,1,2]
    print("I won't join lately, and temp value is", x)
"""
o/p :
I won't join lately, and temp value is 0
I won't join lately, and temp value is 1
I won't join lately, and temp value is 2
"""
for temp in range(3): # [0,1,2]
    print("In iteration ",temp + 1,"I won't join lately, and temp value is", temp)

"""
o/p :
In iteration  1 I won't join lately, and temp value is 0
In iteration  2 I won't join lately, and temp value is 1
In iteration  3 I won't join lately, and temp value is 2
"""