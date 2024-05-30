from .. import db
#Importamos de python 2 funciones
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'  # Nombre de la tabla en plural
    
    usuarioID = db.Column(db.Integer, primary_key=True, autoincrement=True)#
    usuario_nombre = db.Column(db.String(100), nullable=False)
    usuario_apellido = db.Column(db.String(100), nullable=False)
    usuario_contraseña = db.Column(db.String(100), nullable=False)
    usuario_email = db.Column(db.String(100), nullable=False, unique=True)
    usuario_telefono = db.Column(db.Integer, nullable=False)
    rol = db.Column(db.String(10), nullable=False, server_default="users")
    #relacion 1:1(Usuario es padre)
    configuraciones = db.relationship("Configuracion", uselist=False, back_populates="usuario", cascade="all, delete-orphan")
    #relacion 1:1(Usuario es padre)
    reseñas = db.relationship("Reseña", uselist=False, back_populates="usuario", cascade="all, delete-orphan") 
    #relacion 1:N(Usuario es padre)
    notificaciones = db.relationship("Notificacion", back_populates="usuario")
    #relacion 1:1(Usuario es padre)
    prestamos = db.relationship("Prestamo",uselist=False, back_populates="usuario", cascade="all, delete-orphan")


    @property
    def plain_password(self):
        raise AttributeError('Password cant be read')
    #Setter de la contraseña toma un valor en texto plano
    # calcula el hash y lo guarda en el atributo password
    
    @plain_password.setter
    def plain_password(self, password):
        self.usuario_contraseña = generate_password_hash(password)
    #Método que compara una contraseña en texto plano con el hash guardado en la db
    def validate_pass(self,password):
        return check_password_hash(self.usuario_contraseña, password)

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
        notificaciones_info = [notificacion.to_json() for notificacion in self.notificaciones]
        try:
            reseña =  self.reseñas.to_json_short()
        except:
            reseña = ""    
        try:
            prestamo = self.prestamo.to_json_short()
        except:
            prestamo = ""    
        Usuario_json = {
            "usuarioID": self.usuarioID,
            "usuario_nombre": self.usuario_nombre,
            "usuario_apellido": self.usuario_apellido,
            "usuario_contraseña": self.usuario_contraseña,
            "usuario_email": self.usuario_email,
            "usuario_telefono": self.usuario_telefono,
            "reseña": reseña,
            "notificaciones": notificaciones_info,
            'prestamo': prestamo
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
        rol = usuario_json.get('rol')
        return Usuario(usuario_nombre=usuario_nombre,
                        usuario_apellido=usuario_apellido,
                        plain_password=usuario_contraseña,
                        usuario_email=usuario_email,
                        usuario_telefono=usuario_telefono,
                        rol=rol
                       ) 