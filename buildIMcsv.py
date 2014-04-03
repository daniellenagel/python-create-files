f1 = open('250_productgroups_list.txt')
f2 = open('250_iteractionmatrix.xlsx', 'a')

lines = f1.readlines()

import random, math
columns = {}
matrix = {}
for i, x in enumerate(lines):
    if i == len(lines) - 1:
        name = x
        end = ""
    else: 
        name = x[0:len(x)-1]
        end = "\n"

    newLine = ''
    if i == 0:
        # create PG row
        newLine += "INTERACTION INDEX|NOT TRACKED"
        for j, y in enumerate(lines):
            col_header = y if j == len(lines)-1 else y[0:len(y)-1]
            columns[j] = col_header
            matrix[col_header] = {}
            newLine += "|"+col_header
        f2.write(newLine+end) 

        # create NOT TRACKED row
        newLine = "NOT TRACKED|0"
        for j, y in enumerate(lines):
            newLine += "|0"
        f2.write(newLine+end) 

    newLine = name+"|0"
    for j, y in enumerate(lines):
        col_name = columns[j]
        # check if assigned an index
        if matrix[name].get(col_name) is not None: 
            idx = matrix[name][col_name]
        # otherwise generate it
        else: 
            idx = str(random.randint(-5, 5))   
            matrix[col_name][name] = idx 
        newLine += "|"+idx
    
    f2.write(newLine+end) 

f1.close()
f2.close()