from numpy import random

inv = 30000
month_inv = 500

for i in range(0,30):
    for j in range(0,12):
        
        if random.uniform(0, 1) > 0.10:
            r = random.normal(0.07, 0.025)
        else:
            r = random.normal(-0.05, 0.025)
        inv = inv*(1+r/12) + month_inv

print(round(inv,2))