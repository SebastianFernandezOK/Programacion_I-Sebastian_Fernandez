from flask_restful import Resource
from flask import request

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
        libro = request.get_json()
        id = int(max(LIBROS.keys()))+1
        LIBROS[id] = libro
        return LIBROS[id], 201

class Libro(Resource): #A la clase libro le indico que va a ser del tipo recurso(Resource)
    #obtener recurso
        
    def get(self, id):
        Libro = db.session.query(LibrosModel).get_or_404(id)
        return Libro.to_json
        #Verifico que exista el libro
       #if int(id) in LIBROS:
            #retorno libro
            #return LIBROS[int(id)]
        #else:
            #return 'Inexiste', 404
    
    #eliminar recurso
    def delete(self, id):
        #Verifico que exista el libro
        if int(id) in LIBROS:
            #elimino libro
            del LIBROS[int(id)]
            return 'Solicitud correcta', 204
        else:
            return 'Inexistente', 404
    
    #Modificar el recurso libro
    def put(self, id):
        if int(id) in LIBROS:
            libro = LIBROS[int(id)]
            data = request.get_json()
            libro.update(data)
            return 'Solicitud correcta', 201
        return 'Inexistente', 404  