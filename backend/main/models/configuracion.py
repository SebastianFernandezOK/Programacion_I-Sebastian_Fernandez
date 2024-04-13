from .. import db

class Configuracion(db.Model):
    configuracionID = db.Column(db.Integer, primary_key=True)
    idioma = db.Column(db.String, nullable=False)
    orden = db.Column(db.String, nullable=False)



    #Convertir objeto en JSON
    def to_json(self):
        Configuracion_json = {
            "configuracionID":self.configuracionID,
            'idioma': str(self.idioma),
            'orden': str(self.orden),
        }
        return Configuracion_json


        