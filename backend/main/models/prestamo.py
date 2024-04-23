from .. import db
from datetime import datetime

class Prestamo(db.Model):
    prestamosID = db.Column(db.Integer, primary_key=True)
    usuarioID = db.Column(db.Integer, nullable=False)
    libroID = db.Column(db.Integer, db.ForeignKey("libro.libroID"), nullable=False)##---->Clave Foranea
    fecha_entrega = db.Column(db.DateTime, nullable=False)
    fecha_devolucion = db.Column(db.DateTime, nullable=False)
    #nombre de la relacion 
    libro = db.relationship("Libro", back_populates="prestamos", cascade="all, delete-orphan")

    def __repr__(self):
        return '<Prestamo: %r >' % (self.prestamosID)


    #Convertir objeto en JSON   
    def to_json(self):
        #self.libro = db.session.query(LibroModel).get_or_404(self.libroID)
        Prestamo_json = {
            "prestamosID": self.prestamosID,
            "usuarioID": self.usuarioID,
            "libroID": self.libroID,
            "fecha_entrega": self.fecha_entrega.strftime("%Y-%m-%d"),      
            "fecha_devolucion": self.fecha_devolucion.strftime("%Y-%m-%d"),
            'libro' : self.libro.to_json()
        }
        return Prestamo_json

    def to_json_complete(self):
        libros= [libro.to_json() for libro in self.libro]
        Prestamo_json = {
            "prestamosID": self.prestamosID,
            "usuarioID": self.usuarioID,
            "libroID": self.libroID,
            "fecha_entrega": self.fecha_entrega.strftime("%Y-%m-%d"),      
            "fecha_devolucion": self.fecha_devolucion.strftime("%Y-%m-%d"),
            'libros': libros
        }
        return Prestamo_json

    def to_json_short(self):
        Prestamo_json = {
            "prestamosID": self.prestamosID,
            "usuarioID": self.usuarioID,

        }
        return Prestamo_json

    @staticmethod
    #Convertir JSON a objeto
    def from_json(prestamo_json):
        prestamosID = prestamo_json.get('prestamosID')
        usuarioID = prestamo_json.get('usuarioID')
        libroID = prestamo_json.get('libroID')
        fecha_entrega = datetime.strptime(prestamo_json.get('fecha_entrega'), '%Y-%m-%d')
        fecha_devolucion = datetime.strptime(prestamo_json.get('fecha_devolucion'), '%Y-%m-%d')
        return Prestamo(prestamosID=prestamosID,
                        usuarioID=usuarioID,
                        libroID=libroID,
                        fecha_entrega=fecha_entrega,
                        fecha_devolucion=fecha_devolucion,
                    )


