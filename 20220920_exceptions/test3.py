

import os
import sys
import datetime

dirs_lst = os.walk("D:\python_basics")


for temp in dirs_lst:
    required_data = temp
    break

for dirs in temp[1]:
    print(dirs)




