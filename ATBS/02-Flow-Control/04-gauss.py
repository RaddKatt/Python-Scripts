# Adds up all of the numbers from 0 to 100
# Written on Python 3.5.1 on Mac

total = 0
for num in range(101):
    oldTotal = total
    oldNum = num
    total += num
    print(str(oldTotal) + ' + ' + str(oldNum) + ' = ' + str(total))
print(total)
