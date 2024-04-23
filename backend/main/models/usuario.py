from .. import db

class Usuario(db.Model):
    usuarioID = db.Column(db.Integer, primary_key=True)
    prestamoID = db.Column(db.Integer, nullable=False)
    usuario_nombre = db.Column(db.String(100), nullable=False)
    usuario_apellido = db.Column(db.String(100), nullable=False)
    usuario_contraseña = db.Column(db.String(100), nullable=False)
    usuario_email = db.Column(db.String(100), nullable=False)
    usuario_telefono = db.Column(db.Integer, nullable=False)
    # Nombre de la relación 
    configuraciones = db.relationship("Configuracion", back_populates="usuario", cascade="all, delete-orphan") 


    def __repr__(self):
        return '<Usuario: %r %r %r >' % (self.usuarioID, self.usuario_nombre, self.usuario_contraseña)
    
    
    def to_json(self):
        usuario_json = {
            "usuarioID": self.usuarioID,
            "prestamoID": self.prestamoID,
            "usuario_nombre": self.usuario_nombre,
            "usuario_apellido": self.usuario_apellido,
            "usuario_contraseña": self.usuario_contraseña,
            "usuario_email": self.usuario_email,
            "usuario_telefono": self.usuario_telefono,
        }
        return usuario_json

    def to_json_complete(self):
        configuraciones = [configuracion.to_json() for configuracion in self.configuraciones]
        Usuario_json = {
            "usuarioID": self.usuarioID,
            "prestamoID": self.prestamoID,
            "usuario_nombre": self.usuario_nombre,
            "usuario_apellido": self.usuario_apellido,
            "usuario_contraseña": self.usuario_contraseña,
            "usuario_email": self.usuario_email,
            "usuario_telefono": self.usuario_telefono,
            "configuraciones": configuraciones
        }
        return Usuario_json

    def to_json_short(self):
        Usuario_json = {
            "usuarioID": self.usuarioID,
            "usuario_nombre": self.usuario_nombre,
            "usuario_apellido": self.usuario_apellido,
        }
        return Usuario_json

    @staticmethod
    def from_json(usuario_json):
        usuarioID = usuario_json.get('usuarioID')
        prestamoID = usuario_json.get('prestamoID')
        usuario_nombre = usuario_json.get('usuario_nombre')
        usuario_apellido = usuario_json.get('usuario_apellido')
        usuario_contraseña = usuario_json.get('usuario_contraseña')
        usuario_email = usuario_json.get('usuario_email')
        usuario_telefono = usuario_json.get('usuario_telefono')
        return Usuario(usuarioID=usuarioID,
                       prestamoID=prestamoID,
                       usuario_nombre=usuario_nombre,
                       usuario_apellido=usuario_apellido,
                       usuario_contraseña=usuario_contraseña,
                       usuario_email=usuario_email,
                       usuario_telefono=usuario_telefono)