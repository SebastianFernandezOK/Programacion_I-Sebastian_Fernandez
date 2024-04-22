from flask_restful import Resource
from flask import request
from .. import db
from main.models import PrestamoModel
from flask import jsonify


PRESTAMOS = {
    1: {'fecha_alquilado':'20/03/2024', 'fecha_limite':'30/03/2024'},
    2: {'fecha_alquilado':'10/4/2024', 'fecha_limite':'20/04/2024'}
}

class Prestamos(Resource):

    def get(self):
        prestamos = db.session.query(PrestamoModel).all()
        return jsonify([prestamo.to_json() for prestamo in prestamos])

    #insertar recurso
    def post(self):
        prestamo = prestamo.from_json(request.get_json())
        db.session.add(prestamo)
        db.session.commit()
        return prestamo.to_json(), 201

    
class Prestamo(Resource):

    def get(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        return prestamo.to_json()

    def delete(self, id):
        prestamo = db.session.query(prestamo).get_or_404(id)
        db.session.delete(prestamo)
        db.session.commit()
        return '', 204

    
    def put(self, id):
        prestamo = db.session.query(prestamo).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(prestamo, key, value)
        db.session.add(prestamo)
        db.session.commit()
        return prestamo.to_json() , 201
