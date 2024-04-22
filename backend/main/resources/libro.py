from flask_restful import Resource
from flask import request
from .. import db
from main.models import LibroModel
from flask import jsonify

#Datos de prueba en JSON
LIBROS = {
    1: {'nombre':'Rey leon', 'categoria':'Drama'},
    2: {'nombre':'El principito', 'categoria':'Misterio'}
}

class Libros(Resource): 
    #obtener lista de los libros

    def get(self):
        return LIBROS
    
    #insertar recurso

    def post(self):
        libro = libro.from_json(request.get_json())
        db.session.add(libro)
        db.session.commit()
        return libro.to_json(), 201

class Libro(Resource): #A la clase libro le indico que va a ser del tipo recurso(Resource)
    #obtener recurso
        
    def get(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        return libro.to_json()

        #Verifico que exista el libro
       #if int(id) in LIBROS:
            #retorno libro
            #return LIBROS[int(id)]
        #else:
            #return 'Inexiste', 404
    
    #eliminar recurso
    def delete(self, id):
        libro = db.session.query(libro).get_or_404(id)
        db.session.delete(libro)
        db.session.commit()
        return '', 204
    #Modificar el recurso libro
    def put(self, id):
        libro = db.session.query(libro).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(libro, key, value)
        db.session.add(libro)
        db.session.commit()
        return libro.to_json() , 201