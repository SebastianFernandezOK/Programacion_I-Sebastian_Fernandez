from .. import db


class Libro(db.Model):
    libroID = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    editorial = db.Column(db.String(100), nullable=False)
    valoracion = db.Column(db.String(100), nullable=False)
   


    #Convertir objeto en JSON
    def to_json(self):
        Libro_json = {
            "libroID":self.libroID,
            'titulo': str(self.titulo),
            "cantidad":self.cantidad,
            'editorial': str(self.editorial),
            'valoracion': str(self.valoracion),
        }
        return Libro_json


        