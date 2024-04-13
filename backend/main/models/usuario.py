from .. import db

class Usuario(db.Model):
    usuarioID = db.Column(db.Integer, primary_key=True)
    prestamoID = db.Column(db.Integer, nullable=False)
    usuario_nombre = db.Column(db.String(100), nullable=False)
    usuario_apellido = db.Column(db.String(100), nullable=False)
    usuario_contraseña = db.Column(db.String(100), nullable=False)
    usuario_email = db.Column(db.String(100), nullable=False)
    usuario_telefono = db.Column(db.Integer, nullable=False)

    def to_json(self):
        Usuario_json = {
            "usuarioID": self.usuarioID,
            "prestamoID": self.prestamoID,
            "usuario_nombre":str(self.usuario_nombre),
            "usuario_apellido":str(self.usuario_apellido),
            "usuario_contraseña":str(self.usuario_contraseña),
            "usuario_email":str(self.usuario_email),
            "usuario_telefono": self.usuario_telefono,
        }
        return Usuario_json