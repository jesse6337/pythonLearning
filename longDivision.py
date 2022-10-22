coefficents = [1,-4,-15,18]
lasti = len(coefficents)-1

constant = coefficents[lasti]
possibleFactors = []
for i in range(1,constant):
    if (constant/i).is_integer():
        possibleFactors.append(i)
sum = 1
def longD(possibleFactorsD):
    for i in range(len(possibleFactors)):
        factor = possibleFactorsD[i]
        previous = 0
        sumlist = []
        for j in range(len(coefficents)):
            sumlist.append(coefficents[j] + previous* factor)
            previous = sumlist[j]
        if sumlist[len(sumlist)-1] == 0:
            finalFactor = factor
            print(sumlist)
            return finalFactor
print("First positive factor(x-{})".format(longD(possibleFactors)))
negativePossitiveFactors = []
for i in possibleFactors:
    negativePossitiveFactors.append(i* -1)  
print("FIrst negative factor(x-{})".format(longD(negativePossitiveFactors)))
