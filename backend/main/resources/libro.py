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
        
        params = request.args
        ### FILTROS ### 
        #Filtrar por titulo
        if request.args.get('titulo'):
            libros = libros.filter(LibroModel.titulo.like('%' + request.args.get('titulo') + '%'))
      
        if 'sortby_titulo' in params:
            # Ordenar por título de forma descendente
            libros = libros.order_by(LibroModel.titulo.desc())
        #Filtrar por editorial
        if request.args.get('editorial'):
            libros = libros.filter(LibroModel.editorial == request.args.get('editorial'))
        if 'sortby_editorial' in params:
            libros = libros.order_by(LibroModel.editorial.desc())
        #Filtrar por valoración
        if request.args.get('cantidad'):
            libros = libros.filter(LibroModel.cantidad == request.args.get('cantidad'))
        if 'sortby_cantidad' in params:
            libros = libros.order_by(LibroModel.cantidad.asc())      
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

    def post(self):
        data = request.get_json()
        autores_ids = data.get('autores', [])  # Obtener los IDs de los autores del JSON o una lista vacía si no se proporcionan
        libro = LibroModel.from_json(data)

        if autores_ids:
            # Obtener las instancias de autores basadas en las IDs recibidas
            autores = AutorModel.query.filter(AutorModel.autorID.in_(autores_ids)).all()
            # Agregar las instancias de autor a la lista de autores del libro
            libro.autores.extend(autores)

        try:
            db.session.add(libro)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"Error al agregar el libro: {str(e)}", 400

        return libro.to_json(), 201 #Si la operación es exitosa, se devuelve la representación JSON del libro con el código de estado 201.

class Libro(Resource): #A la clase libro le indico que va a ser del tipo recurso(Resource)
    #obtener recurso        
    def get(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        return libro.to_json_complete()

    def delete(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        try:
            db.session.delete(libro)
            db.session.commit()
            return {"message": "Eliminado correctamente"}, 200
        except Exception as e:
            db.session.rollback()
            return f"Error al borrar el libro: {str(e)}", 400
        return libro.to_json(), 201

    def put(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        data = request.get_json()
        for key, value in data.items():
            setattr(libro, key, value)
        try:
            db.session.add(libro)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"Error al agregar el libro: {str(e)}", 400
        return libro.to_json(), 201
