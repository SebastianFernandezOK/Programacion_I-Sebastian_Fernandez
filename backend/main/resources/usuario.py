from flask_restful import Resource
from flask import request
from .. import db
from main.models import UsuarioModel, NotificacionModel, PrestamoModel
from flask import jsonify

#Datos de prueba en JSON
USUARIOS = {
    1: {'nombre':'Sebastián', 'apellido':'Fernández'},
    2: {'nombre':'Augusto', 'apellido':'Giuffrida'}
}

class Usuarios(Resource): 
    def get(self):
        #Página inicial por defecto
        page = 1
        #Cantidad de elementos por página por defecto
        per_page = 10
        
        usuarios = db.session.query(UsuarioModel)
        
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        ### FILTROS ###
        # Filtrar por nombre 
        if request.args.get('nombre'):
            usuarios = usuarios.filter(UsuarioModel.usuario_nombre.like(f"%{request.args.get('nombre')}%"))       
        # Filtrar por apellido 
        if request.args.get('apellido'):
            usuarios = usuarios.filter(UsuarioModel.usuario_apellido.like(f"%{request.args.get('apellido')}%"))     
        # Filtrar por número de préstamos 
        if request.args.get('nr_prestamos'):
                    # Subquery para contar el número de préstamos por usuario. subconsulta que cuenta el número de préstamos por usuario
                    subquery = db.session.query(PrestamoModel.usuarioID, func.count(PrestamoModel.prestamosID).label('total_prestamos')).group_by(PrestamoModel.usuarioID).subquery()
                    # Join con la subquery y ordenamiento por el número de préstamos, 
                    usuarios = usuarios.join(subquery, UsuarioModel.usuarioID == subquery.c.usuarioID).order_by(subquery.c.total_prestamos.desc())

        ### FIN FILTROS ####     
          
        #Obtener valor paginado
        usuarios = usuarios.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({"usuarios":[usuario.to_json() for usuario in usuarios.items],    
                  'total': usuarios.total,
                  'pages': usuarios.pages,
                  'page': page      
        })

    #insertar recurso
    def post(self):
        usuario = UsuarioModel.from_json(request.get_json())
        notificaciones_ids = request.get_json().get('notificaciones')

        if notificaciones_ids:
            # Obtener las instancias de notificaciones basadas en las ids recibidas
            notificaciones = NotificacionModel.query.filter(NotificacionModel.id.in_(notificaciones_ids)).all()
            # Agregar las instancias de notificacion al usuario
            usuario.notificaciones.extend(notificaciones) 

        try:
            db.session.add(usuario)
            db.session.commit()
        except:
            db.session.rollback()
            return "Formato incorrecto", 400    
        return usuario.to_json(), 201

    
class Usuario(Resource): #A la clase usuario le indico que va a ser del tipo recurso(Resource)
    #obtener recurso
        
    def get(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        return usuario.to_json()

    #eliminar recurso
    def delete(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        try:
            db.session.delete(usuario)
            db.session.commit()
        except:
            db.session.rollback()
            return "Formato incorrecto", 400    
        return usuario.to_json() , 204

    #Modificar el recurso animal
    def put(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        data = request.get_json()
        for key, value in data.items():
            setattr(usuario, key, value)
        try:
            db.session.add(usuario)
            db.session.commit()
        except:
            db.session.rollback()
            return "Formato incorrecto", 400    
        return usuario.to_json() , 201
