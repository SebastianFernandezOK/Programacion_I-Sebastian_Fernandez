from .. import db
from datetime import datetime

class Prestamo(db.Model):
    __tablename__ = 'prestamos'  # Nombre de la tabla en plural

    prestamosID = db.Column(db.Integer, primary_key=True)
    usuarioID = db.Column(db.Integer, db.ForeignKey('usuarios.usuarioID'), nullable=False) # Clave Foranea
    libroID = db.Column(db.Integer, db.ForeignKey("libros.libroID"), nullable=False)  # Clave Foranea
    fecha_entrega = db.Column(db.DateTime, nullable=False)
    fecha_devolucion = db.Column(db.DateTime, nullable=False)
    # nombre de la relación 
    libro = db.relationship("Libro", back_populates="prestamos", single_parent=True)
    usuario = db.relationship("Usuario", back_populates="prestamos")




    def __repr__(self):
        return '<Prestamo: %r >' % (self.prestamosID)

    # Convertir objeto en JSON   
    def to_json(self):
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
        libros_info = [libro.to_json() for libro in self.libros]
        usuarios_info = [usuario.to_json() for usuario in self.usuarios]
        Prestamo_json = {
            "prestamosID": self.prestamosID,
            "usuarioID": self.usuarioID,
            "libroID": self.libroID,
            "fecha_entrega": self.fecha_entrega.strftime("%Y-%m-%d"),      
            "fecha_devolucion": self.fecha_devolucion.strftime("%Y-%m-%d"),
            'libros': libros_info,
            "usuarios": usuarios_info,
        }
        return Prestamo_json

    def to_json_short(self):
        Prestamo_json = {
            "prestamosID": self.prestamosID,
            "usuarioID": self.usuarioID,

        }
        return Prestamo_json

    @staticmethod
    # Convertir JSON a objeto
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