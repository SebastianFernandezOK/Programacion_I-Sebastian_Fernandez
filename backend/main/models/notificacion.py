from .. import db

class Notificacion(db.Model):
    notificacionID = db.Column(db.Integer, primary_key=True)
    comentario = db.Column(db.String(100), nullable=False)
    usuarioID = db.Column(db.Integer, db.ForeignKey("usuario.usuarioID"), nullable=False)##---->Clave Foranea
    # Nombre de la relación 
    usuarios = db.relationship("Usuario", back_populates="notificacion", cascade="all, delete-orphan") 

    def __repr__(self):
        return '<Notificacion: %r >' % self.notificacionID

    def to_json(self):
        Notificacion_json = {
            "notificacionID": self.notificacionID,
            "usuarioID":self.usuarioID,
            "comentario":str(self.comentario),
        }
        return Notificacion_json

    def to_json_complete(self):
        usuarios = [usuario.to_json() for usuario in self.usuarios]
        Notificacion_json = {
            "notificacionID": self.notificacionID,
            "comentario":str(self.comentario),
            "usuarioID": self.usuarioID,
            'usuarios': usuarios
        }
        return Notificacion_json

    def to_json_short(self):
        Notificacion_json = {
            "notificacionID": self.notificacionID,
            "usuarioID": self.usuarioID,
        }
        return Notificacion_json

    @staticmethod
    def from_json(notificacion_json):
        notificacionID = notificacion_json.get('notificacionID')
        usuarioID = notificacion_json.get('usuarioID')
        comentario = notificacion_json.get('comentario')
        return Notificacion(notificacionID=notificacionID,
                            usuarioID=usuarioID, 
                            comentario=comentario)