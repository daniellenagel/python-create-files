f1 = open('250_productgroups_list.txt')
f2 = open('250_productgroups.csv', 'a')

lines = f1.readlines()

def toDec(x):
    return (math.ceil(x*100)/100)

import random, math

for i, x in enumerate(lines):
    if i == len(lines) - 1:
        name = x
        end = ""
    else: 
        name = x[0:len(x)-1]
        end = "\n"
    units = random.randint(10000, 100000)
    margin = toDec(random.uniform(2, 8) * units)
    f2.write(name+"|"+
        name+" description|"+ 
        str(random.randint(1,9))+"|"+ # priority 
        str(toDec(random.uniform(0.01, 0.99)))+"|"+ # elasticity 
        str(units)+"|"+
        str(margin)+"|"+
        str(toDec(random.uniform(0.01, 0.99)))+"|"+ # margin 
        str(toDec(random.uniform(-0.99, 0.99)))+ # organic growth
        end) 

f1.close()
f2.close()