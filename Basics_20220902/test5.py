
flat_201 = "office"
flat_101 = "market"
flat_301 = "walking"
flat_501 = "jogging"

if flat_201 == "available" : # "office" == "available" False
    print("Deliver to 201")
elif flat_101 == "available" : # "market" == "available"
    print("Deliver to 101")
elif flat_501 == "available" : # "jogging" == "available"
    print("Deliver to 501")
elif flat_301 == "available" : # "walking" == "available"
    print("Deliver to 301")
else:
    print("Deliver to watchmen")

