from .. import db
from datetime import datetime

   
libros_prestamos = db.Table("libros_prestamos",
    db.Column("libroID",db.Integer,db.ForeignKey("libros.libroID"),primary_key=True),
    db.Column("prestamosID",db.Integer,db.ForeignKey("prestamos.prestamoID"),primary_key=True)
    )     

class Libro(db.Model):

    __tablename__ = 'libros'  # Nombre de la tabla en plural

    libroID = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    editorial = db.Column(db.String(100), nullable=False)
    #relacion N:M(Libro es padre)
    prestamos = db.relationship('Prestamo', secondary=libros_prestamos, backref=db.backref('libros', lazy='dynamic'))
    #prestamos = db.relationship("Prestamo", uselist=False, back_populates="libros", cascade="all, delete-orphan") 
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
        }
        return Libro_json

    # Convertir objeto en JSON completo con lista de prestamos y reseñas
    def to_json_complete(self):
        prestamos_info = [prestamo.to_json() for prestamo in self.prestamos]
        autores_info = [{"autor_nombre": autor.autor_nombre, "autor_apellido": autor.autor_apellido} for autor in self.autores]
        reseñas_info = [reseña.to_json() for reseña in self.reseñas]
        Libro_json = {
            "libroID": self.libroID,
            'titulo': self.titulo,
            "cantidad": self.cantidad,
            'editorial': self.editorial,
            'prestamos': prestamos_info,
            "autores": autores_info,
            "reseñas": reseñas_info,
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
        return Libro(libroID=libroID,
                    titulo=titulo,
                    cantidad=cantidad,
                    editorial=editorial)
