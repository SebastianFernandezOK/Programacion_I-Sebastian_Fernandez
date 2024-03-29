from flask_restful import Resource
from flask import request

VALORACION = {
    1: {'valoracion':'5 estrellas'}
    
}

COMENTARIOS = {
    1: {'comentario':'buen libro'} 
}



class Valoraciones(Resource):

    def get(self):
        return VALORACION

    def put(self, id):
        if int(id) in VALORACION:
            valoracion = VALORACION[int(id)]
            data = request.get_json()
            valoracion.update(data)
            return '', 201
        return '', 404
    

class Comentarios(Resource):

    def get(self):
        return COMENTARIOS

    def put(self, id):
        if int(id) in COMENTARIOS:
            comentario = COMENTARIOS[int(id)]
            data = request.get_json()
            comentario.update(data)
            return '', 201
        return '', 404    