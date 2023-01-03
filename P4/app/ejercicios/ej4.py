import re


def encontrarApellido(cadena):
    patron1 = re.compile('([A-Za-z]+) ([A-Z])')
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
    if matcher:
        return matcher.group(0)
    else:
        matcher = encontrarCorreo(cadena)
        if matcher:
            return matcher.group(0)
        else:
            matcher = encontrarTarjeta(cadena)
            if matcher:
                return matcher.group(0)
            else:
                return 'No se ha encontrado ninguna coincidencia'


    
































