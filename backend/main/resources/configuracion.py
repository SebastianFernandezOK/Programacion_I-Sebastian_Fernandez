from flask_restful import Resource
from flask import request

CONFIGURACION = {
    1: {'modos oscuro':'si','idioma':'ingles'}
    
}

class Configuraciones(Resource):

    def get(self):
        
        Configuracion = db.session.query(ConfiguracionModel).get_or_404(id)
        return Configuracion_json

        #return CONFIGURACION

    def post(self):
        configuracion = request.get_json()
        id = int(max(CONFIGURACION.keys()))+1
        CONFIGURACION[id] = configuracion
        return CONFIGURACION[id], 201 