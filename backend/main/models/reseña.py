from .. import db

class Reseña(db.Model):
    __tablename__ = 'reseñas'  # Nombre de la tabla en plural

    reseñaID = db.Column(db.Integer, primary_key=True)
    usuarioID = db.Column(db.Integer, db.ForeignKey("usuarios.usuarioID"), nullable=False)  # Clave Foranea
    libroID = db.Column(db.Integer, db.ForeignKey("libros.libroID"), nullable=False)  # Clave Foranea
    valoracion = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.String(100), nullable=False)  
    # Relación con Usuario
    usuario = db.relationship("Usuario", back_populates="reseñas")
    # Relación con Libro
    libro = db.relationship("Libro", back_populates="reseñas")

    def __repr__(self):
        return '<Reseña: %r >' % self.reseñaID

    def to_json(self):
        Reseña_json = {
            "reseñaID": self.reseñaID,
            "usuarioID": self.usuarioID,
            "libroID": self.libroID,
            "valoracion": self.valoracion,
            "comentario": self.comentario,
        }
        return Reseña_json

    def to_json_complete(self):
        usuario_info = self.usuario.to_json()
        libro_info = self.libro.to_json()
        Reseña_json = {
            "reseñaID": self.reseñaID,
            "valoracion": self.valoracion,
            "comentario": self.comentario,
            "usuario": usuario_info,
            "libro": libro_info,
        }
        return Reseña_json

    # Convertir objeto en JSON corto
    def to_json_short(self):
        Reseña_json = {
            "reseñaID": self.reseñaID,
            "libroID": self.libroID,
            "valoracion": self.valoracion,
        }
        return Reseña_json

    # Convertir JSON a objeto
    @staticmethod
    def from_json(reseña_json):
        reseñaID = reseña_json.get('reseñaID')
        usuarioID = reseña_json.get('usuarioID')
        libroID = reseña_json.get('libroID')
        valoracion = reseña_json.get('valoracion')
        comentario = reseña_json.get('comentario')
        return Reseña(reseñaID=reseñaID,
                      usuarioID=usuarioID,
                      libroID=libroID,
                      valoracion=valoracion,
                      comentario=comentario)