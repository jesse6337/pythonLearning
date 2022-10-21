import math


coefficents = [1,-5,-22,56]
lasti = len(coefficents)-1

constant = coefficents[lasti]
possibleFactors = []
for i in range(1,constant):
    if (constant/i).is_integer():
        possibleFactors.append(i)
sum = 1
for i in range(len(possibleFactors)):
    factor = possibleFactors[i]
    previous = 0
    sumlist = []
    for j in range(len(coefficents)):
        sumlist.append(coefficents[j] + previous* factor)
        previous = sumlist[j]
    if sumlist[len(sumlist)-1] == 0:
        finalFactor = factor
        break
print(finalFactor)
        


