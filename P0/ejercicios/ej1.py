import math


print("Por favor, inserte un número entero:")
n = int(input())

numbers = []
for i in range(0, n+1):
    numbers.append(i)

for i in range(2, int(math.sqrt(n))+1):
    if(numbers[i]!=0):
        a = int(n/i)
        for j in range(i, a+1):
            numbers[i*j] = 0


for i in range (0, n):
    if(numbers[i]!=0):
        print(numbers[i])