from flask_restful import Resource
from flask import request
from .. import db
from main.models import ConfiguracionModel
from flask import jsonify

CONFIGURACION = {
    1: {'modos oscuro':'si','idioma':'ingles'}
    
}

class Configuraciones(Resource):

    def get(self):
        configuraciones = db.session.query(ConfiguracionModel).all()
        return jsonify([configuraciones.to_json() for configuracion in configuraciones])

    #insertar recurso
    def post(self):
        configuracion = configuracion.from_json(request.get_json())
        db.session.add(configuracion)
        db.session.commit()
        return configuracion.to_json(), 201