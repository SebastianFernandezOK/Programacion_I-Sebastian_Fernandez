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
        #Página inicial por defecto
        page = 1
        #Cantidad de elementos por página por defecto
        per_page = 10
        
        #no ejecuto el .all()
        prestamos = db.session.query(PrestamoModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        ### FILTROS ###     
        ### FIN FILTROS ####     
          
        #Obtener valor paginado
        prestamos = prestamos.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({"prestamos":[prestamo.to_json() for prestamo in prestamos],    
                  'total': prestamos.total,
                  'pages': prestamos.pages,
                  'page': page      
        })

    #insertar recurso
    def post(self):
        prestamo = PrestamoModel.from_json(request.get_json())
        try:
            db.session.add(prestamo)
            db.session.commit()
        except:
            db.session.rollback()
            return "Formato incorrecto", 400    
        return prestamo.to_json(), 201

    
class Prestamo(Resource):

    def get(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        return prestamo.to_json()

    def delete(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        try:
            db.session.delete(prestamo)
            db.session.commit()
        except:
            db.session.rollback()
            return "Formato incorrecto", 400
        return '', 204
   
    def put(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        data = request.get_json() #obtener el diccionario completo
        for key, value in data.items():  # Usar items() para iterar sobre las claves y valores
            setattr(prestamo, key, value)
        try:    
            db.session.add(prestamo)
            db.session.commit()
        except:
            db.session.rollback()
            return "Formato incorrecto", 400    
        return prestamo.to_json() , 201
