from flask_restful import Resource
from flask import request

PRESTAMOS = {
    1: {'fecha_alquilado':'20/03/2024', 'fecha_limite':'30/03/2024'},
    2: {'fecha_alquilado':'10/4/2024', 'fecha_limite':'20/04/2024'}
}

class Prestamos(Resource):

    def get(self):
        return PRESTAMOS
    
    
    def post(self):
        prestamo = request.get_json()
        id = int(max(PRESTAMOS.keys()))+1
        PRESTAMOS[id] = prestamo
        return PRESTAMOS[id], 201
    
class Prestamo(Resource):

    def get(self, id):
        #Verifico que exista el prestamo
        if int(id) in PRESTAMOS:
            #retorno prestamo
            return PRESTAMOS[int(id)]
        else:
            return 'Inexistente', 404
    #eliminar recurso
    def delete(self, id):
        #Verifico que exista el prestamo
        if int(id) in PRESTAMOS:
            #elimino prestamo
            del PRESTAMOS[int(id)]
            return 'Solicitud correcta', 204
        else:
            return 'Inexistente', 404
    #Modificar el recurso prestamo
    def put(self, id):
        if int(id) in PRESTAMOS:
            prestamo = PRESTAMOS[int(id)]
            data = request.get_json()
            prestamo.update(data)
            return 'Solicitud correcta', 201
        return 'Inexistente', 404
