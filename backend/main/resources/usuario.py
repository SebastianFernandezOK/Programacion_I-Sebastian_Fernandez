from flask_restful import Resource
from flask import request

#Datos de prueba en JSON
USUARIOS = {
    1: {'nombre':'Sebastián', 'apellido':'Fernández'},
    2: {'nombre':'Augusto', 'apellido':'Giuffrida'}
}

class Usuarios(Resource): 
    #obtener lista de los usuarios

    def get(self):
        return USUARIOS
    
    #insertar recurso

    def post(self):
        usuario = request.get_json()
        id = int(max(USUARIOS.keys()))+1
        USUARIOS[id] = usuario
        return USUARIOS[id], 201
    
class Usuario(Resource): #A la clase usuario le indico que va a ser del tipo recurso(Resource)
    #obtener recurso
        
    def get(self, id):
        #Verifico que exista el usuario
        if int(id) in USUARIOS:
            #retorno usuario
            return USUARIOS[int(id)]
        else:
            return 'Inexistente', 404
    
    #eliminar recurso
    def delete(self, id):
        #Verifico que exista el usuario
        if int(id) in USUARIOS:
            #elimino usuario
            del USUARIOS[int(id)]
            return 'Solicitud correcta', 204
        else:
            return 'Inexistente', 404
    
    #Modificar el recurso usuario
    def put(self, id):
        if int(id) in USUARIOS:
            usuario = USUARIOS[int(id)]
            data = request.get_json()
            usuario.update(data)
            return 'Solicitud correcta', 201
        return 'Inexistente', 404