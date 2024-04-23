from .. import db

class Reseña(db.Model):
    reseñaID = db.Column(db.Integer, primary_key=True)
    usuarioID = db.Column(db.Integer, db.ForeignKey("usuario.usuarioID"), nullable=False)  # Clave Foranea
    libroID = db.Column(db.Integer, db.ForeignKey("libro.libroID"), nullable=False)  # Clave Foranea
    valoracion = db.Column(db.Integer, nullable=False)
    comentario = db.Column(db.String(100), nullable=False)
    
    # Relación con Usuario
    usuarios = db.relationship("Usuario", back_populates="reseñas")
    # Relación con Libro
    libros = db.relationship("Libro", back_populates="reseñas")
    
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
        usuarios_info = [usuario.to_json() for usuario in self.usuarios]
        libros_info = [libro.to_json() for libro in self.libros]
        Reseña_json = {
            "reseñaID": self.reseñaID,
            "usuarios": usuarios_info,
            "libros": libros_info,
            "valoracion": self.valoracion,
            "comentario": self.comentario,
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