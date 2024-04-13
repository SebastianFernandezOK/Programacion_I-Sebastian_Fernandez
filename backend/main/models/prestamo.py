from .. import db

class Prestamo(db.Model):
    prestamosID = db.Column(db.Integer, primary_key=True)
    usuarioID = db.Column(db.Integer, nullable=False)
    libroID = db.Column(db.Integer, nullable=False)
    fecha_entrega = db.Column(db.Date, nullable=False)
    fecha_devolucion = db.Column(db.Date, nullable=False)

    def to_json(self):
        Prestamo_json = {
            "prestamosID": self.prestamosID,
            "usuarioID": self.usuarioID,
            "libroID": self.libroID,
            "fecha_entrega": self.fecha_entrega.strftime("%Y-%m-%d"),      
            "fecha_devolucion": self.fecha_devolucion.strftime("%Y-%m-%d"),
        }
        return Prestamo_json