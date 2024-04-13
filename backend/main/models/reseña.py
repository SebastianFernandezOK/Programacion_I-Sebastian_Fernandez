from .. import db

class Reseña(db.Model):
    reseñaID = db.Column(db.Integer, primary_key=True)
    usuarioID = db.Column(db.Integer, nullable=False)
    libroID = db.Column(db.Integer, nullable=False)
    valoracion = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.String(100), nullable=False)

    def to_json(self):
        Reseña_json = {
            "reseñaID": self.reseñaID,
            "usuarioID": self.usuarioID,
            "libroID": self.libroID,
            "valoracion": self.valoracion,
            "comentario":str(self.comentario),
        }
        return Reseña_json