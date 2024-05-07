from datetime import datetime
import sqlite3

# Conectarse a la base de datos existente
conn = sqlite3.connect('D:\\User\\Desktop\\code\\programacion\\Programacion_I-Sebastian_Fernandez\\backend\\DB\\biblioteca.db')

# Crear un cursor para ejecutar consultas
cur = conn.cursor()

# Generar automáticamente los datos para la tabla "usuarios"
datos_usuarios = []
for i in range(1, 31):  # Genera datos para 30 usuarios
    usuarioID = i
    usuario_nombre = f'Nombre{i}'
    usuario_apellido = f'Apellido{i}'
    usuario_contraseña = f'contraseña{i}'
    usuario_email = f'email{i}@example.com'
    usuario_telefono = 123456789 + i
    configuracionID = 200 + i
    datos_usuarios.append((usuarioID, usuario_nombre, usuario_apellido, usuario_contraseña, usuario_email, usuario_telefono))

# Insertar datos en la tabla "usuarios"
cur.executemany('''
    INSERT INTO usuarios (
        usuarioID,
        usuario_nombre,
        usuario_apellido,
        usuario_contraseña,
        usuario_email,
        usuario_telefono
    ) VALUES (?, ?, ?, ?, ?, ?)
''', datos_usuarios)

# Generar automáticamente los datos para la tabla "libros"
datos_libros = []
for i in range(1, 31):  # Genera datos para 30 libros
    libroID = 1000 + i  # Suma una cantidad constante para obtener IDs únicos
    titulo = f'Título del Libro {i}'
    cantidad = i * 2  # Cantidad variable
    editorial = f'Editorial {i}'
    valoracion = f'Valoración del Libro {i}'
    datos_libros.append((libroID, titulo, cantidad, editorial))

# Insertar datos en la tabla "libros"
cur.executemany('''
    INSERT INTO libros (libroID, titulo, cantidad, editorial) VALUES (?, ?, ?, ?)
''', datos_libros)

# Generar automáticamente los datos para la tabla "autores"
datos_autores = []
for i in range(1, 31):  # Genera datos para 30 autores
    autorID = i
    libroID = 1000 + i  # ID de libro generado anteriormente
    autor_nombre = f'Autor Nombre {i}'
    autor_apellido = f'Autor Apellido {i}'
    datos_autores.append((autorID, libroID, autor_nombre, autor_apellido))

# Insertar datos en la tabla "autores"
cur.executemany('''
    INSERT INTO autores (autorID, libroID, autor_nombre, autor_apellido) VALUES (?, ?, ?, ?)
''', datos_autores)

# Generar automáticamente los datos para la tabla "configuraciones"
datos_configuraciones = []
for i in range(1, 31):  # Genera datos para 30 configuraciones
    configuracionID = i
    idioma = f'Idioma {i}'
    orden = f'Orden {i}'
    usuario_id = i  # ID de usuario generado anteriormente
    datos_configuraciones.append((configuracionID, idioma, orden, usuario_id))

# Insertar datos en la tabla "configuraciones"
cur.executemany('''
    INSERT INTO configuraciones (configuracionID, idioma, orden, usuario_id) VALUES (?, ?, ?, ?)
''', datos_configuraciones)

# Generar automáticamente los datos para la tabla "reseñas"
datos_reseñas = []
for i in range(1, 31):  # Genera datos para 30 reseñas
    reseñaID = i
    usuarioID = i
    libroID = 1000 + i  # ID de libro generado anteriormente
    valoracion = i % 5 + 1  # Valoración de 1 a 5
    comentario = f'Comentario {i}'
    datos_reseñas.append((reseñaID, usuarioID, libroID, valoracion, comentario))

# Insertar datos en la tabla "reseñas"
cur.executemany('''
    INSERT INTO reseñas (reseñaID, usuarioID, libroID, valoracion, comentario) VALUES (?, ?, ?, ?, ?)
''', datos_reseñas)

# Generar automáticamente los datos para la tabla "prestamos"
datos_prestamos = []
for i in range(1, 31):  # Genera datos para 30 préstamos
    prestamoID = i
    usuarioID = i
    libroID = 1000 + i  # ID de libro generado anteriormente
    fecha_entrega = datetime.now()
    fecha_devolucion = datetime.now()
    datos_prestamos.append((prestamoID, usuarioID, libroID, fecha_entrega, fecha_devolucion))

# Insertar datos en la tabla "prestamos"
cur.executemany('''
    INSERT INTO prestamos (prestamoID, usuarioID, libroID, fecha_entrega, fecha_devolucion) VALUES (?, ?, ?, ?, ?)
''', datos_prestamos)

# Generar automáticamente los datos para la tabla "notificaciones"
datos_notificaciones = []
for i in range(1, 31):  # Genera datos para 30 notificaciones
    notificacionID = i
    comentario = f'Comentario de la notificación {i}'
    usuarioID = i  # ID de usuario generado anteriormente
    datos_notificaciones.append((notificacionID, comentario, usuarioID))

# Insertar datos en la tabla "notificaciones"
cur.executemany('''
    INSERT INTO notificaciones (notificacionID, comentario, usuarioID) VALUES (?, ?, ?)
''', datos_notificaciones)

datos_notificaciones_usuarios = []
for i in range(1, 31):  # Genera datos para 30 notificaciones_usuarios
    notificacionID = i
    usuarioID = i
    datos_notificaciones_usuarios.append((notificacionID, usuarioID))

# Insertar datos en la tabla intermedia "notificaciones_usuarios"
cur.executemany('''
    INSERT INTO notificaciones_usuarios (notificacionID, usuarioID) VALUES (?, ?)
''', datos_notificaciones_usuarios)

# Generar automáticamente los datos para la tabla "libros_autores"
datos_libros_autores = []
for i in range(1, 31):  # Genera datos para 30 libros_autores
    libroID = i
    autorID = i
    datos_libros_autores.append((libroID, autorID))

# Insertar datos en la tabla "libros_autores"
cur.executemany('''
    INSERT INTO libros_autores (libroID, autorID) VALUES (?, ?)
''', datos_libros_autores)

# Generar automáticamente los datos para la tabla "libros_prestamos"
datos_libros_prestamos = []
for i in range(1, 31):  # Genera datos para 30 libros_prestamos
    libroID = 1000 + i  # ID de libro generado anteriormente
    prestamosID = 100 + i  # ID de préstamo generado anteriormente
    datos_libros_prestamos.append((libroID, prestamosID))

# Insertar datos en la tabla "libros_prestamos"
cur.executemany('''
    INSERT INTO libros_prestamos (libroID, prestamosID) VALUES (?, ?)
''', datos_libros_prestamos)


# Guardar los cambios
conn.commit()

# Cerrar la conexión
conn.close()

print("Datos insertados correctamente en la base de datos existente.")