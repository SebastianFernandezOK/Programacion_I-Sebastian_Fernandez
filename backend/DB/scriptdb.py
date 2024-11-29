from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
from faker import Faker
import sqlite3
import random

# Inicializar Faker para generación de datos
fake = Faker()

# Conectarse a la base de datos existente
conn = sqlite3.connect('C:\\Users\\MegaTecnologia\\Documents\\Programacion_I-Sebastian_Fernandez\\backend\\DB\\biblioteca.db')
cur = conn.cursor()

# Crear un archivo de log para registrar los datos
log_file = 'db.log'
with open(log_file, 'w') as log:
    log.write(f'LOG DE DATOS INSERTADOS - {datetime.now()}\n\n')

    # Generar datos para la tabla "usuarios"
    datos_usuarios = []
    datos_usuarios.append((32, "pepe", "pepe", generate_password_hash("pepe"), "pepe@pepe.pepe", "123456789", "admin"))
    log.write(f'ID: {1}, Nombre: {"pepe"}, Apellido: {"pepe"}, psk: {"pepe"}, Email: {"pepe@pepe.pepe"}, Telefono: {"123456789"}, Rol: {"admin"}\n')
    log.write('\n')
    for i in range(1, 31):
        usuarioID = i
        usuario_nombre = fake.first_name()
        usuario_apellido = fake.last_name()
        usuario_contraseña = fake.password()
        usuario_email = fake.email()
        usuario_telefono = fake.phone_number()
        rol = fake.random_element(elements=('admin', 'user', 'librarian'))
        datos_usuarios.append((usuarioID, usuario_nombre, usuario_apellido, generate_password_hash(usuario_contraseña), usuario_email, usuario_telefono, rol))
        log.write(f'ID: {usuarioID}, Nombre: {usuario_nombre}, Apellido: {usuario_apellido}, psk: {usuario_contraseña}, Email: {usuario_email}, Telefono: {usuario_telefono}, Rol: {rol}\n')
    log.write('\n')

    # Insertar datos en la tabla "usuarios"
    cur.executemany('''
        INSERT INTO usuarios (
            usuarioID,
            usuario_nombre,
            usuario_apellido,
            usuario_contraseña,
            usuario_email,
            usuario_telefono,
            rol
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', datos_usuarios)

    # Generar datos para la tabla "libros"
    datos_libros = []
    for i in range(1, 31):
        libroID = 1000 + i
        titulo = fake.sentence(nb_words=3)
        cantidad = fake.random_int(min=1, max=20)
        editorial = fake.company()
        genero = fake.word()
        image = f'image{random.randint(0, 8)}.jpg'
        datos_libros.append((libroID, titulo, cantidad, editorial, genero, image))


    # Insertar datos en la tabla "libros"
    cur.executemany('''
        INSERT INTO libros (libroID, titulo, cantidad, editorial, genero, image) VALUES (?, ?, ?, ?, ?, ?)
    ''', datos_libros)

    # Generar datos para la tabla "autores"
    datos_autores = []
    for i in range(1, 31):
        autorID = i
        autor_nombre = fake.first_name()
        autor_apellido = fake.last_name()
        datos_autores.append((autorID, autor_nombre, autor_apellido))

    # Insertar datos en la tabla "autores"
    cur.executemany('''
        INSERT INTO autores (autorID, autor_nombre, autor_apellido) VALUES (?, ?, ?)
    ''', datos_autores)

    # Generar datos para la tabla "configuraciones"
    datos_configuraciones = []
    for i in range(1, 31):
        configuracionID = i
        idioma = fake.language_name()
        orden = fake.word()
        usuario_id = i
        datos_configuraciones.append((configuracionID, idioma, orden, usuario_id))

    # Insertar datos en la tabla "configuraciones"
    cur.executemany('''
        INSERT INTO configuraciones (configuracionID, idioma, orden, usuario_id) VALUES (?, ?, ?, ?)
    ''', datos_configuraciones)

    # Generar datos para la tabla "reseñas"
    datos_reseñas = []
    reseñaID = 1  
    for libroID in range(1001, 1031):  
        num_reseñas = random.randint(1, 6)  # Determinar cuántas reseñas generar para cada libro
        for _ in range(num_reseñas):
            usuarioID = random.randint(1, 30)  # Seleccionar un usuario aleatorio
            valoracion = fake.random_int(min=1, max=5)
            comentario = fake.text(max_nb_chars=100)
            datos_reseñas.append((reseñaID, usuarioID, libroID, valoracion, comentario))
            reseñaID += 1  

    # Insertar datos en la tabla "reseñas"
    cur.executemany('''
        INSERT INTO reseñas (reseñaID, usuarioID, libroID, valoracion, comentario) VALUES (?, ?, ?, ?, ?)
    ''', datos_reseñas)


    # Generar datos para la tabla "prestamos"
    datos_prestamos = []
    for i in range(1, 31):
        prestamoID = i
        usuarioID = i
        libroID = 1000 + i
        fecha_entrega = fake.date_between(start_date='-1y', end_date='today')
        fecha_devolucion = fecha_entrega + timedelta(days=fake.random_int(min=7, max=30))
        datos_prestamos.append((prestamoID, usuarioID, libroID, fecha_entrega, fecha_devolucion))

    # Insertar datos en la tabla "prestamos"
    cur.executemany('''
        INSERT INTO prestamos (prestamoID, usuarioID, libroID, fecha_entrega, fecha_devolucion) VALUES (?, ?, ?, ?, ?)
    ''', datos_prestamos)

    # Generar datos para la tabla "notificaciones"
    datos_notificaciones = []
    for i in range(1, 31):
        notificacionID = i
        comentario = fake.sentence(nb_words=6)
        usuarioID = i
        datos_notificaciones.append((notificacionID, comentario, usuarioID))

    # Insertar datos en la tabla "notificaciones"
    cur.executemany('''
        INSERT INTO notificaciones (notificacionID, comentario, usuarioID) VALUES (?, ?, ?)
    ''', datos_notificaciones)

    # Generar datos para la tabla intermedia "notificaciones_usuarios"
    datos_notificaciones_usuarios = []
    for i in range(1, 31):
        notificacionID = i
        usuarioID = i
        datos_notificaciones_usuarios.append((notificacionID, usuarioID))

    # Insertar datos en la tabla "notificaciones_usuarios"
    cur.executemany('''
        INSERT INTO notificaciones_usuarios (notificacionID, usuarioID) VALUES (?, ?)
    ''', datos_notificaciones_usuarios)

    # Generar datos para la tabla "libros_autores"
    datos_libros_autores = []
    for i in range(1, 31):
        libroID = 1000 + i
        autorID = i
        datos_libros_autores.append((libroID, autorID))

    # Insertar datos en la tabla "libros_autores"
    cur.executemany('''
        INSERT INTO libros_autores (libroID, autorID) VALUES (?, ?)
    ''', datos_libros_autores)



# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Datos insertados correctamente en la base de datos existente.")
