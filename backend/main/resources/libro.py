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
        #Página inicial por defecto
        page = 1
        #Cantidad de elementos por página por defecto
        per_page = 10
        
        #no ejecuto el .all()
        libros = db.session.query(LibroModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        ### FILTROS ###     
        ### FIN FILTROS ####     
          
        #Obtener valor paginado
        libros = libros.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'libros': [libro.to_json() for libro in libros],
                  'total': libros.total,
                  'pages': libros.pages,
                  'page': page
                })
   
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