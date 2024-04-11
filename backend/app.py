from main import create_app
import os
from main import db
#funcion que retorna la app
app = create_app()

# Con esto la app esta disponible en todo los archivos
# Nos permite no tener conflictos con referencias circulares

app.app_context().push()

if __name__ == '__main__':
    db.create_all
    app.run(debug=True,port=os.getenv('PORT'))