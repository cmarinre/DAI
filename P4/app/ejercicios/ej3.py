
from operator import truediv
import random
import string


def balanceadaFunction(cadena):

    n = len(cadena)-1 
    contador = 0
    salir = False
    i=0

    if((n%2)!=0):   
        while (i<(n+1) and salir==False):
            if(cadena[i]=='['): 
                contador+=1
            else:
                contador-=1
            if(contador<0):
                salir = True
            i+=1
    else:
        salir = True
        
    if(contador!=0):
        salir = True

    if(salir==True):
        return('Incorrecto')
    else:
        return('Correcto')







