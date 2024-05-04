from flask_restful import Resource
from flask import request
from main.models import UsuarioModel
from .. import db

USUARIOS = {
    1: {'nombre':'Sebastián', 'apellido':'Fernández'},
    2: {'nombre':'Augusto', 'apellido':'Giuffrida'}
}

class SignIn(Resource):

    def post(self):
        usuario = UsuarioModel.from_json(request.get_json())
        try:
            db.session.add(usuario)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"Error al agregar la configuración: {str(e)}", 400
        return configuracion.to_json(), 201
 
class Login(Resource):
    
    def post(self):
        usuario = UsuarioModel.from_json(request.get_json())
        try:
            db.session.add(usuario)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"Error al agregar la configuración: {str(e)}", 400
        return configuracion.to_json(), 201
        
        #usuario = request.get_json()
        #id = int(max(USUARIOS.keys()))+1
        #USUARIOS[id] = usuario
        #return USUARIOS[id], 201  
 