from flask_restful import Resource
from flask import request

NOTIFICACION = {
    1: {'nombre':'libro_nuevo','Descripcion':'Salio un libro nuevo'}
    
}

class Notificaciones(Resource):

    def post(self):
        notificacion = request.get_json()
        id = int(max(NOTIFICACION.keys()))+1
        NOTIFICACION[id] = notificacion
        return NOTIFICACION[id], 201 