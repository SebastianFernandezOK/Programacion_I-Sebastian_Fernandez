from flask_restful import Resource
from flask import request
from .. import db
from main.models import ReseñaModel
from flask import jsonify

VALORACION = {
    1: {'valoracion':'5 estrellas'}
    
}

COMENTARIOS = {
    1: {'comentario':'buen libro'} 
}



class Valoraciones(Resource):

    def get(self):
        reseñas = db.session.query(ReseñaModel).all()
        return jsonify([reseña.to_json() for reseña in reseñas])
        #return VALORACION

    def post(self):
        reseña = ReseñaModel.from_json(request.get_json())
        try:
            db.session.add(reseña)
            db.session.commit()
        except:
            db.session.rollback()
            return "Formato incorrecto", 400            
        return reseña.to_json(), 201


class Comentarios(Resource):
    def get(self):
        comentarios = db.session.query(ReseñaModel).all()
        return jsonify([comentario.to_json() for comentario in comentarios])
    
    def post(self):
        comentario = ReseñaModel.from_json(request.get_json())
        try:
            db.session.add(comentario)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"Error al agregar la configuración: {str(e)}", 400
        return comentario.to_json(), 201