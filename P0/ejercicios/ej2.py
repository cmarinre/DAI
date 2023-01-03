
def fibonacci(m):
    m = int(m)
    if(m>1):
        return fibonacci(m-1) + fibonacci(m-2)
    else:
        if (m==1):
            return 1
        else:
            if (m==0):
                return 0


archivo =  open("./numero.txt","r")
n = archivo.readline()
archivo.close()
numero = int(n)
archivo2 = open("./respuesta.txt", "a")
sol = fibonacci(numero)
archivo2.write(str(sol))

