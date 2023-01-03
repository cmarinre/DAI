import re


def encontrarApellido():
    patron1 = re.compile('([A-Za-z]+) ([A-Z])')

    print("Por favor, inserte una cadena:")
    cadena = input()
    matcher = patron1.search(cadena)
    print(matcher)

def encontrarCorreo():
    patronCorreo = re.compile('[A-Za-z0-9]+@[a-z]+\.[a-z]+')

    print("Por favor, inserte una cadena:")
    cadena = input()
    matcher = patronCorreo.search(cadena)
    print(matcher)


def encontrarTarjeta():
    patronTarjeta = re.compile('\d{4} \d{4} \d{4} \d{4}|\d{4}-\d{4}-\d{4}-\d{4}')

    print("Por favor, inserte una cadena:")
    cadena = input()
    matcher = patronTarjeta.search(cadena)
    print(matcher)

encontrarTarjeta()































