import re


def encontrarApellido(cadena):
    patron1 = re.compile('[A-Za-z]+ [A-Z]\s')
    matcher = patron1.search(cadena)
    return(matcher)

def encontrarCorreo(cadena):
    patronCorreo = re.compile('[A-Za-z0-9]+@[a-z]+\.[a-z]+')
    matcher = patronCorreo.search(cadena)
    return(matcher)

def encontrarTarjeta(cadena):
    patronTarjeta = re.compile('\d{4} \d{4} \d{4} \d{4}|\d{4}-\d{4}-\d{4}-\d{4}')
    matcher = patronTarjeta.search(cadena)
    return(matcher)

def expresionRegularFunction(cadena):
    matcher = encontrarApellido(cadena)
    print(matcher)
    if matcher:
        print('1')
        return matcher
    else:
        matcher = encontrarCorreo(cadena)
        print(matcher)
        if matcher:
            print('2')
            return matcher
        else:
            matcher = encontrarTarjeta(cadena)
            print(matcher)
            if matcher:
                print('3')
                return matcher
            else:
                return 'No se ha encontrado ninguna coincidencia'


expresionRegularFunction('5467-5648-5485-5486')

