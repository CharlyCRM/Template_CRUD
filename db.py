from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Configuramos el Engine
# Engine permite a SQLalchemy conectarse a la base de datos
engine = create_engine('sqlite:///database/personas.db') # Definimos la BBDD si existe nos conectamos y si no existe la crea

# Configuramos la sesión - Nos permite realizar transacciones (operaciones) dentro de la BBDD
Session = sessionmaker(bind=engine) # Creamos una sesión
session = Session()

# Indicamos al ORM que debe transformas las clases en tablas
Base = declarative_base() # Esta instrucción transforma las clases en tablas, pero debemos especificar en que clases debe aplicarlo.