from flask_restful import Resource
from flask import request
from .. import db

VALORACION = {
    1: {'valoracion':'5 estrellas'}
    
}

COMENTARIOS = {
    1: {'comentario':'buen libro'} 
}



class Valoraciones(Resource):

    def get(self):
        Reseña= db.session.query(ReseñaModel).get_or_404(id)
        return Reseña_json

        #return VALORACION

    def put(self, id):
        if int(id) in VALORACION:
            valoracion = VALORACION[int(id)]
            data = request.get_json()
            valoracion.update(data)
            return 'Solicitud correcta', 201
        return 'Inexistente', 404
    

class Comentarios(Resource):

    def get(self):
       Reseña= db.session.query(ReseñaModel).get_or_404(id)
       return Reseña_json

        #return COMENTARIOS

    def put(self, id):
        if int(id) in COMENTARIOS:
            comentario = COMENTARIOS[int(id)]
            data = request.get_json()
            comentario.update(data)
            return 'Solicitud correcta', 201
        return 'Inexistente', 404    