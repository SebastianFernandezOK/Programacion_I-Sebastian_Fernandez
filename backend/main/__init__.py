from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
#Importar Flask JWT
from flask_jwt_extended import JWTManager
##Forma de organizar una aplicacion web con modulos en flask

api=Api() #Iniciar Api de flask_restful
db=SQLAlchemy() #Iniciar SQLAlchemy

#Inicializar Migrate
migrate = Migrate()

#Inicializar JWT
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    load_dotenv() #Se cargan variables del archivo .env
    

    #if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')): ## LINUX
        #os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))           ##


    # Configuración de SQLAlchemy
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False                                                                    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getenv('DATABASE_PATH'), os.getenv('DATABASE_NAME'))
    db.init_app(app)

    with app.app_context():  # Entrar en el contexto de la aplicación Flask                           ##
        # Crear la base de datos si no existe (Solo válido si se utiliza SQLite)                      ##WINDOWS
        if not os.path.exists(os.path.join(os.getenv('DATABASE_PATH'), os.getenv('DATABASE_NAME'))):  ##
            db.create_all()

    import main.resources as resources

    api.add_resource(resources.UsuariosResources, '/usuarios')
    api.add_resource(resources.UsuarioResources, '/usuario/<id>')

    api.add_resource(resources.LibrosResources, '/libros')
    api.add_resource(resources.LibroResources, '/libro/<id>')

    api.add_resource(resources.SignInResources, '/signin')
    api.add_resource(resources.LoginResources, '/login')

    api.add_resource(resources.PrestamosResources, '/prestamos')
    api.add_resource(resources.PrestamoResources, '/prestamo/<id>')

    api.add_resource(resources.NotificacionesResources, '/notificaciones')

    api.add_resource(resources.ConfiguracionesResources, '/configuraciones')

    api.add_resource(resources.ReseñasResources, '/reseñas')
    api.add_resource(resources.ReseñaResources, '/reseña/<id>')

    api.add_resource(resources.AutoresResources, '/autores')
    api.add_resource(resources.AutorResources, '/autor/<id>')

    api.init_app(app)
    
#Cargar clave secreta
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    #Cargar tiempo de expiración de los tokens
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    jwt.init_app(app)

    from main.auth import routes
    #Importar blueprint
    app.register_blueprint(routes.auth) ##Forma de organizar una aplicacion web con modulos en flask

    #Por ultimo retornamos la aplicacion iniializado
    return app