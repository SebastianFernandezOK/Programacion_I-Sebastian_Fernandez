from .. import db
from datetime import datetime

class Libro(db.Model):
    libroID = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    editorial = db.Column(db.String(100), nullable=False)
    valoracion = db.Column(db.String(100), nullable=False)        
    # nombre de la relación 
    autores = db.relationship("Autor", back_populates="libro", cascade="all, delete-orphan")    
    prestamos = db.relationship("Prestamo", back_populates="libro", cascade="all, delete-orphan")
   
    def __repr__(self):
        return '<Libro: %r  >' % (self.libroID)

    # Convertir objeto en JSON
    def to_json(self):
        Libro_json = {
            "libroID": self.libroID,
            'titulo': self.titulo,
            "cantidad": self.cantidad,
            'editorial': self.editorial,
            'valoracion': self.valoracion,
        }
        return Libro_json

    # Convertir objeto en JSON completo con lista de prestamos
    def to_json_complete(self):
        prestamos = [prestamo.to_json() for prestamo in self.prestamos]
        autores_info = [{"autor_nombre": autor.autor_nombre, "autor_apellido": autor.autor_apellido} for autor in self.autores]
        Libro_json = {
            "libroID": self.libroID,
            'titulo': self.titulo,
            "cantidad": self.cantidad,
            'editorial': self.editorial,
            'valoracion': self.valoracion,
            'prestamos': prestamos,
            "autores": autores_info,
        }
        return Libro_json

    # Convertir objeto en JSON corto
    def to_json_short(self):
        Libro_json = {
            "libroID": self.libroID,
            "titulo": self.titulo,
        }
        return Libro_json

    # Convertir JSON a objeto
    @staticmethod
    def from_json(libro_json):
        libroID = libro_json.get('libroID')
        titulo = libro_json.get('titulo')
        cantidad = libro_json.get('cantidad')
        editorial = libro_json.get('editorial')
        valoracion = libro_json.get('valoracion')
        return Libro(libroID=libroID,
                    titulo=titulo,
                    cantidad=cantidad,
                    editorial=editorial, 
                    valoracion=valoracion)
