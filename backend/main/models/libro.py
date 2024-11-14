from .. import db
from datetime import datetime

   

class Libro(db.Model):

    __tablename__ = 'libros'  # Nombre de la tabla en plural

    libroID = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    editorial = db.Column(db.String(100), nullable=False)
    genero = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String, nullable=False)
    #relacion 1:M(Libro es padre)
    prestamos =  db.relationship('Prestamo', back_populates='libro', cascade='all, delete-orphan') 
    #relacion 1:N(Libro es padre)
    reseñas =  db.relationship('Reseña', back_populates='libro', cascade='all, delete-orphan')
    #relacion N:M(Libro es padre)
    #autores = db.relationship("Autor", secondary="libros_autores", back_populates="libros")

    def __repr__(self):
        return '<Libro: %r  >' % (self.libroID)

    # Convertir objeto en JSON
    def to_json(self):
        Libro_json = {
            "libroID": self.libroID,
            'titulo': self.titulo,
            "cantidad": self.cantidad,
            'editorial': self.editorial,
            'genero': self.genero,
            "image": self.image
        }
        return Libro_json

    # Convertir objeto en JSON completo con lista de prestamos y reseñas
    def to_json_complete(self):
        prestamos = [prestamo.to_json_short() for prestamo in self.prestamos]
        autores = [autor.to_json() for autor in self.autores]
        reseñas = [reseña.to_json_short() for reseña in self.reseñas]

        Libro_json = {
            "libroID": self.libroID,
            'titulo': self.titulo,
            "cantidad": self.cantidad,
            'editorial': self.editorial,
            'genero': self.genero,
            "image": self.image,
            'prestamos': prestamos,
            "autores": autores,
            "resenas": reseñas,
        }
        return Libro_json  

    # Convertir objeto en JSON corto
    def to_json_short(self):
        Libro_json = {
            "libroID": self.libroID,
            "titulo": self.titulo,
            "image": self.image,
            "genero": self.genero,
        }
        return Libro_json

    # Convertir JSON a objeto
    @staticmethod
    def from_json(libro_json):
        libroID = libro_json.get('libroID')
        titulo = libro_json.get('titulo')
        cantidad = libro_json.get('cantidad')
        editorial = libro_json.get('editorial')
        genero = libro_json.get('genero')
        image = libro_json.get('image')
        return Libro(libroID=libroID,
                    titulo=titulo,
                    cantidad=cantidad,
                    editorial=editorial,
                    genero=genero,
                    image=image
                    )
