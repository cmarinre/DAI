#./app/app.py
from cgitb import reset
from dataclasses import field
from flask import Flask, Response
from flask import render_template
from flask import request, jsonify
from bson.json_util import dumps
from pymongo import MongoClient
from bson import ObjectId
from flask_restful import Resource, Api


import math
from ejercicios.ej1 import erastotenesFunction
from ejercicios.ej2 import fibonacciFunction
from ejercicios.ej3 import balanceadaFunction
from ejercicios.ej4 import expresionRegularFunction


app = Flask(__name__)
api = Api(app)

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



############# P2.1 ############

# Conectar al servicio (docker) "mongo" en su puerto estandar
client = MongoClient("mongo", 27017)

# Base de datos
db = client.cockteles

@app.route('/todas_las_recetas')
def mongo():
    # Encontramos los documentos de la coleccion "recipes"
    recetas = db.recipes.find() # devuelve un cursor(*), no una lista ni un iterador

    lista_recetas = []
    for  receta in recetas:
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')




@app.route('/recetas_de/<string:cadena>')
def mongo2(cadena):

    recetas = db.recipes.find( { "name": { "$regex": cadena, "$options": 'i' } } ) # devuelve un cursor(*), no una lista ni un iterador
  #  recetas = db.recipes.find( { "name":  cadena } ) # devuelve un cursor(*), no una lista ni un iterador

    lista_recetas = []
    for  receta in recetas:
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')




@app.route('/recetas_con/<string:cadena>')
def mongo3(cadena):

    recetas = db.recipes.find( { "ingredients.name": { "$regex": cadena, "$options": 'i' } } ) # devuelve un cursor(*), no una lista ni un iterador

    lista_recetas = []
    for  receta in recetas:
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')




@app.route('/recetas_compuestas_de/<int:n>/ingredientes')
def mongo4(n):

    recetas = db.recipes.find( { "ingredients": { "$size": n } } )
    # devuelve un cursor(*), no una lista ni un iterador

    lista_recetas = []
    for  receta in recetas:
        lista_recetas.append(receta)

    response = {
        'len': len(lista_recetas),
        'data': lista_recetas
    }

    # Convertimos los resultados a formato JSON
    resJson = dumps(response)

    # Devolver en JSON al cliente cambiando la cabecera http para especificar que es un json
    return Response(resJson, mimetype='application/json')




############### PRACTICA 2.2 #################



# para devolver una lista (GET), o añadir (POST)
@app.route('/api/recipes/', methods=['GET', 'POST'])
def api_1():
    if request.method == 'GET':
        buscados = db.recipes.find().sort('name')
        return Response(dumps(buscados), mimetype='application/json')

    elif request.method == 'POST':
        
        request_data = request.get_json()
        db.recipes.insert_one(request_data)
        nuevo_dato = db.recipes.find_one({}, request_data)
        return Response(dumps(nuevo_dato), mimetype='application/json')




# para devolver una, modificar o borrar
@app.route('/api/recipes/<id>/', methods=['GET', 'PUT', 'DELETE'])
def api_2(id):
    if request.method == 'GET':

        buscado = db.recipes.find_one({'_id': ObjectId(id)})
        if buscado:
            return Response(dumps(buscado), mimetype='application/json')

        else:
            return jsonify({'error':'Not found'}), 404


    elif request.method == 'PUT':

        buscado = db.recipes.find_one({'_id':ObjectId(id)})
        if buscado:
            request_data = request.get_json()
            db.recipes.update_one({'_id': ObjectId(id)}, {'$set': request_data})
            modificado = db.recipes.find_one({'_id':ObjectId(id)})
            return Response(dumps(modificado), mimetype='application/json')
        else:
            return jsonify({'error':'Not found'}), 404

    elif request.method == 'DELETE':
        buscado = db.recipes.find_one({'_id':ObjectId(id)})
        if buscado:
            db.recipes.delete_one({'_id': ObjectId(id)})
            return Response(dumps(id), mimetype='application/json')
        else:
            return jsonify({'error':'Not found'}), 404




#"""
class api_restful_1(Resource):
    def get(self):
        lista = []
        buscados = db.recipes.find().sort('name')
        for recipe in buscados:
            recipe['_id'] = str(recipe['_id']) # casting a string (es un ObjectId)
            lista.append(recipe)
        response = {
            'len': len(lista),
            'data': lista
        }
        resJson = dumps(response)
        return Response(resJson, mimetype='application/json')
        
    def post(self):
        request_data = request.get_json()
        db.recipes.insert_one(request_data)
        nuevo_dato = db.recipes.find_one({'_id':ObjectId(request_data['_id'])})

        resJson = dumps(nuevo_dato)
        return Response(resJson, mimetype='application/json')

api.add_resource(api_restful_1, "/api_restful_1")
#"""


#"""
class api_restful_2(Resource):
    def get(self, id):

        buscado = db.recipes.find_one({'_id':ObjectId(id)})
        if buscado:
            buscado['_id'] = str(buscado['_id']) # casting a string (es un ObjectId)
            response = {
                'len': len(buscado),
                'data': buscado
            }
            resJson = dumps(response)
            return Response(resJson, mimetype='application/json')

        else:
            return jsonify({'error':'Not found'}), 404

    def put(self, id):
        buscado = db.recipes.find_one({'_id':ObjectId(id)})
        if buscado:

            request_data = request.get_json()

            if 'name' in request_data:
                buscado['name'] = request_data['name']
            if 'ingredients' in request_data:
                buscado['ingredients'] = request_data['ingredients']
            if 'garnish' in request_data:
                buscado['garnish'] = request_data['garnish']
            if 'instructions' in request_data:
                buscado['instructions'] = request_data['instructions']
            if 'slug' in request_data:
                buscado['slug'] = request_data['slug']
            
            db.recipes.replace_one({'_id': ObjectId(id)}, buscado)
            modificado = db.recipes.find_one({'_id':ObjectId(id)})

            response = {
                'len': len(modificado),
                'data': modificado
            }
            resJson = dumps(response)
            return Response(resJson, mimetype='application/json')
        else:

            return jsonify({'error':'Not found'}), 404


    def delete(self, id):

        buscado = db.recipes.find_one({'_id':ObjectId(id)})
        if buscado:
            db.recipes.delete_one({'_id': id})
            return id
        else:
            return jsonify({'error':'Not found'}), 404





api.add_resource(api_restful_2, "/api_restful_2/<id>/")
#"""






