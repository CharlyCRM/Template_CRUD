from sqlalchemy import Column, Integer, String, Boolean
import db # Este es el nombre de nuestro fichero bd.py Esto nos permite acceder a ese fichero desde aquí

class Persona(db.Base): # Este Base hace referencia a la variable del fichero bd
    __tablename__ = "persona" # Indicamos el nombre de la table para el ORM
    '''Indicamos que atributos de la clase persona, formarán parte de la tabla, los cuales
        se convertiran en las columnas de la BBDD'''
    __table_args__ = {'sqlite_autoincrement': True} # Automaticamente todas las columnas definidas como Primary Key convierte en autoincremental
    id_persona = Column(Integer, primary_key = True) # Definimos la columna Primary Key
    nombre = Column(String, nullable = False) # El campo nombre, no puede estar vacio
    edad = Column(Integer)

    def __init__(self, nombre, edad): # La estructura de la clase, corresponde a la misma estructura que la BBDD
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return "Persona ({} , {})".format(self.nombre, self.edad)

