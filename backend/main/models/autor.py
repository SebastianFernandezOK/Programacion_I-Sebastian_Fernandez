from .. import db

class Autor(db.Model):
    autorID = db.Column(db.Integer, primary_key=True)
    libroID = db.Column(db.Integer, nullable=False)
    autor_nombre = db.Column(db.String(100), nullable=False)
    autor_apellido = db.Column(db.String(100), nullable=False)


    def to_json(self):
        Autor_json = {
            "autorID": self.autorID,
            "libroID": self.libroID,
            "autor_nombre":str(self.autor_nombre),
            "autor_apellido":str(self.autor_apellido),            
        }
        return Autor_json