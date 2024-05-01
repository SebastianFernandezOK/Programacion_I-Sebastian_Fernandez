from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import LibroModel, AutorModel

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
        libros = db.session.query(LibroModel)#obtener todos objetos de la tabla en la base base de datos


        if request.args.get('page'): ##Existe el parametro "page" en la request?
            page = int(request.args.get('page'))##Si existe, lo cargo
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        ### FILTROS ###     
        ### FIN FILTROS ####     
          
        #Obtener valor paginado(evita que se traigan todos los registros)
        libros = libros.paginate(page=page, per_page=per_page, error_out=True)
                                                                #Si no existe la pag
                                                                #devuelve un error

        return jsonify({'libros': [libro.to_json() for libro in libros],
                  'total': libros.total, #
                  'pages': libros.pages, # Esto se tiene que enviar al backend para paginar
                  'page': page           #
                })
   
    #insertar recurso
    def post(self):
        data = request.get_json()
        autores_ids = data.get('autores', [])
        libro = LibroModel.from_json(data)

        if autores_ids:
            # Obtener las instancias de autores basadas en las ids recibidas
            autores = AutorModel.query.filter(AutorModel.id.in_(autores_ids)).all()
            # Agregar las instancias de autor a la lista de autores del libro
            libro.autores.extend(autores)
            
        try:
            db.session.add(libro)
            db.session.commit()
        except:
            return "Formato incorrecto", 400

        return libro.to_json(), 201

class Libro(Resource): #A la clase libro le indico que va a ser del tipo recurso(Resource)
    #obtener recurso        
    def get(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        return libro.to_json()

     # Eliminar recurso
    def delete(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        db.session.delete(libro)
        db.session.commit()
        return '', 204

    #Modificar el recurso libro
    def put(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        data = request.get_json()

        for key, value in data.items():
            setattr(libro, key, value)

        try:
            db.session.add(libro)
            db.session.commit()
        except:
            return "Formato incorrecto", 400

        return libro.to_json(), 201
