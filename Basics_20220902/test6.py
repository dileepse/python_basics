
flat_201 = "office"
flat_101 = "market"
flat_301 = "unavailable"
flat_501 = "available"

if flat_201 == "available" : # "office" == "available" False
    print("Deliver to 201")
else:
    print("Deliver to watchman")
if flat_101 == "available" : # "market" == "available"
    print("Deliver to 101")
if flat_501 == "available" : # "available" == "available"
    print("Deliver to 501")
if flat_301 == "available" :
    print("Deliver to 301")