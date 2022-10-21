import math

list = [i for i in range(1000)]
sum = 0
for i in range(2, 10):
    for j in range(2, math.ceil(i/2)):
        x = i/j
        if  x.is_integer():
            pass
    print(sum)
