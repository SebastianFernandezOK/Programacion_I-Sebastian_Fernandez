from flask_restful import Resource
from flask import request, jsonify
from .. import db



NOTIFICACION = {
    1: {'nombre':'libro_nuevo','Descripcion':'Salio un libro nuevo'}
    
}

class Notificaciones(Resource):

    def post(self):
        Notificacion= db.session.query(NotificacionModel).get_or_404(id)
        return Notificacion_json
        
        
        #notificacion = request.get_json()
        #id = int(max(NOTIFICACION.keys()))+1
        #NOTIFICACION[id] = notificacion
        #return NOTIFICACION[id], 201 