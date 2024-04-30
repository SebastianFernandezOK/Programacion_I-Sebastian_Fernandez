from flask_restful import Resource
from flask import request

USUARIOS = {
    1: {'nombre':'Sebastián', 'apellido':'Fernández'},
    2: {'nombre':'Augusto', 'apellido':'Giuffrida'}
}

class SignIn(Resource):

    def post(self):
        usuario = usuario.from_json(request.get_json())
        try:
            db.session.add(usuario)
            db.session.commit()
        except:
            return "Formato incorrecto", 400    
        return usuario.to_json(), 201

        #usuario = request.get_json()
        #id = int(max(USUARIOS.keys()))+1
        #USUARIOS[id] = usuario
        #return USUARIOS[id], 201  
 
    

class Login(Resource):
    
    def post(self):
        usuario = usuario.from_json(request.get_json())
        try:
            db.session.add(usuario)
            db.session.commit()
        except:
            return "Formato incorrecto", 400    
        return usuario.to_json(), 201
        
        #usuario = request.get_json()
        #id = int(max(USUARIOS.keys()))+1
        #USUARIOS[id] = usuario
        #return USUARIOS[id], 201  
 