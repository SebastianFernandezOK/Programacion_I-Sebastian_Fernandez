from .. import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'  # Nombre de la tabla en plural
    
    usuarioID = db.Column(db.Integer, primary_key=True, autoincrement=True)#
    usuario_nombre = db.Column(db.String(100), nullable=False)
    usuario_apellido = db.Column(db.String(100), nullable=False)
    usuario_contraseña = db.Column(db.String(100), nullable=False)
    usuario_email = db.Column(db.String(100), nullable=False)
    usuario_telefono = db.Column(db.Integer, nullable=False)
    #relacion 1:1(Usuario es padre)
    configuracion = db.relationship("Configuracion", uselist=False, back_populates="usuario", cascade="all, delete-orphan")
    #relacion 1:1(Usuario es padre)
    reseñas = db.relationship("Reseña", uselist=False, back_populates="usuario", cascade="all, delete-orphan") 
    #relacion 1:N(Usuario es padre)
    notificaciones = db.relationship("Notificacion", back_populates="usuario")
    #relacion 1:1(Usuario es padre)
    prestamos = db.relationship("Prestamo",uselist=False, back_populates="usuario", cascade="all, delete-orphan")

    def __repr__(self):
        return '<Usuario: %r %r %r >' % (self.usuarioID, self.usuario_nombre, self.usuario_contraseña)
    
    
    def to_json(self):
        usuario_json = {
            "usuarioID": self.usuarioID,
            "usuario_nombre": self.usuario_nombre,
            "usuario_apellido": self.usuario_apellido,
            "usuario_contraseña": self.usuario_contraseña,
            "usuario_email": self.usuario_email,
            "usuario_telefono": self.usuario_telefono,
        }
        return usuario_json

    def to_json_complete(self):
        configuraciones_info = [configuracion.to_json() for configuracion in self.configuraciones]
        reseñas_info = [reseña.to_json() for reseña in self.reseñas]
        notificaciones_info = [notificacion.to_json() for notificacion in self.notificaciones]
        prestamos_info = self.prestamos
        Usuario_json = {
            "usuarioID": self.usuarioID,
            "usuario_nombre": self.usuario_nombre,
            "usuario_apellido": self.usuario_apellido,
            "usuario_contraseña": self.usuario_contraseña,
            "usuario_email": self.usuario_email,
            "usuario_telefono": self.usuario_telefono,
            "configuraciones": configuraciones_info,
            "reseñas": reseñas_info,
            "notificaciones": notificaciones_info,
            'prestamos': prestamos_info,
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
        usuario_nombre = usuario_json.get('usuario_nombre')
        usuario_apellido = usuario_json.get('usuario_apellido')
        usuario_contraseña = usuario_json.get('usuario_contraseña')
        usuario_email = usuario_json.get('usuario_email')
        usuario_telefono = usuario_json.get('usuario_telefono')
        prestamoID = usuario_json.get('prestamoID')  # Obtener prestamoID del JSON
        return Usuario(usuario_nombre=usuario_nombre,
                        usuario_apellido=usuario_apellido,
                        usuario_contraseña=usuario_contraseña,
                        usuario_email=usuario_email,
                        usuario_telefono=usuario_telefono,
                        prestamoID=prestamoID) 