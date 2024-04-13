from .. import db

class Notificacion(db.Model):
    notificacionID = db.Column(db.Integer, primary_key=True)
    comentario = db.Column(db.String(100), nullable=False)
    usuarioID = db.Column(db.Integer, nullable=False)

    def to_json(self):
        Notificacion_json = {
            "notificacionID": self.notificacionID,
            "usuarioID":self.usuarioID,
            "comentario":str(self.comentario),
        }
        return Notificacion_json