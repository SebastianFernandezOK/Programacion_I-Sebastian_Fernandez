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
        data = request.get_json()
        notificacion = NotificacionModel.from_json(data) #notificacion = notificacion.from_json(request.get_json()

        try:
            db.session.add(notificacion)
            db.session.commit()

        except Exception as error: # captura cualquier excepción que ocurra durante la ejecución del código en el bloque try,
            db.session.rollback()  #realiza un rollback de la sesión y luego devuelve el mensaje de error junto con el código de estado 400.      
            return str(error), 400 # Esto garantiza que cualquier cambio no se guarde en la base de datos si ocurre un error.
                                   
        return notificacion.to_json(), 201
        
        

#Cuando ocurre una excepción durante la ejecución del código dentro de un bloque try, 
#es una buena práctica realizar un rollback de la sesión de la base de datos para 
#deshacer cualquiercambio realizado desde el inicio de la transacción actual.
#Esto asegura que la base de datos no quede en un estado inconsistente.

#rollback() se llama para deshacer cualquier cambio realizado en la sesión de la base de datos. 
#Esto asegura que la base de datos mantenga su integridad en caso de error.

        #notificacion = request.get_json()
        #id = int(max(NOTIFICACION.keys()))+1
        #NOTIFICACION[id] = notificacion
        #return NOTIFICACION[id], 201 