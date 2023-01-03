import math


def erastotenesFunction(m):    
    n = int(m)

    numbers = []
    for i in range(0, n+1):
        numbers.append(i)

    for i in range(2, int(math.sqrt(n))+1):
        if(numbers[i]!=0):
            a = int(n/i)
            for j in range(i, a+1):
                numbers[i*j] = 0

    cadena = ''
    for i in range (0, n):
        if(numbers[i]!=0):
            cadena = cadena + ' ' + str(numbers[i])

    return cadena