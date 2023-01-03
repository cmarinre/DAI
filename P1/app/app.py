#./app/app.py
from flask import Flask
from flask import render_template
import math
from ejercicios.ej1 import erastotenesFunction
from ejercicios.ej2 import fibonacciFunction
from ejercicios.ej3 import balanceadaFunction
from ejercicios.ej4 import expresionRegularFunction

app = Flask(__name__)
          

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/erastotenes/<int:n>')
def erastotenes(n):
    return erastotenesFunction(n)

@app.route('/fibonacci/<int:n>')
def fibonacci(n):
    return str(fibonacciFunction(n))

@app.route('/balanceada/<string:cadena>')
def balanceada(cadena):
    return balanceadaFunction(cadena)

@app.route('/expresionRegular/<string:cadena>')
def expresionRegular(cadena):
    return str(expresionRegularFunction(cadena))

@app.route('/imagen')
def imagen():
    return render_template('images.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

