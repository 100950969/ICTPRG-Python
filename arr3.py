values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
total = 0
i = 0
while i < len(values):
    total = total + values[i]
    i = i + 1

add1 = sum(values)
print('The sum of these numbers is: ', add1)

ave = total / len(values)
print('The average of these numbers is: ', ave)

max1 = max(values)
print('The biggest number is: ', max1)