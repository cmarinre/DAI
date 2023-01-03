
from operator import truediv
import random
import string

cadena = []
n=5

for i in range(1, n):
    num = ''.join(random.sample(string.digits, 1))
    if((int(num)%2)==0):
        cadena.append('[')
    else:
        cadena.append("]")

print(cadena)

contador = 0
salir = False
i=0

if((n%2)!=0):
    while (i<(n-1) and salir==False):
        if(cadena[i]=='['):
            contador+=1
        else:
            contador-=1
        if(contador<0):
            salir = True
        print(i)
        i+=1
else:
    salir = True
    
if(contador!=0):
    salir = True

if(salir==True):
    print('Incorrecto')
else:
    print('Correcto')







