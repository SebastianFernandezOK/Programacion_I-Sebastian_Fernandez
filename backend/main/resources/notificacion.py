from flask_restful import Resource
from flask import request
from .. import db
from main.models import NotificacionModel
from flask import jsonify



NOTIFICACION = {
    1: {'nombre':'libro_nuevo','Descripcion':'Salio un libro nuevo'}
    
}

class Notificaciones(Resource):

    def post(self):
        notificacion = notificacion.from_json(request.get_json())
        try:
            db.session.add(notificacion)
            db.session.commit()
        except:
            return "Formato incorrecto", 400    
        return notificacion.to_json(), 201
        
        
        #notificacion = request.get_json()
        #id = int(max(NOTIFICACION.keys()))+1
        #NOTIFICACION[id] = notificacion
        #return NOTIFICACION[id], 201 