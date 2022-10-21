x = input()
y = int(x)
even = []
for i in range(y):
    if (i/2).is_integer():
        even.append(i)
this = len(even)
print(this-1)