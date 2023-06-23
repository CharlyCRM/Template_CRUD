from sqlalchemy import and_, or_, text
import db
import sys
from models import Persona

def agregarPersonasIniciales():  # Función que simplemente crea unos objetos de la clase Persona
    p1 = Persona("Cristian", 20)
    p2 = Persona("Maria", 30)
    p3 = Persona("Sara", 20)
    p4 = Persona("Daniel", 35)
    p5 = Persona("John", 18)
    p6 = Persona("Eva", 20)

    #db.Session.add(p1) # Esta sintaxis añade el objeto p1 a la BD
    db.session.add_all([p1, p2, p3, p4, p5, p6]) # Esta sintaxis añade todos los objetos en una LISTA que le pasemos como argumento
    db.session.commit() # Sintaxis para que los cambios se apliquen a la BB
    db.session.close() # Cerramos la BD

def consultasDePrueba():
    print("\n #1. Obtener un objeto a partir de su id (su Primary Key) Si no lo encuentra, devuelve None")
    result = db.session.get(Persona, 2) # Indicamos como argumento el nombre de la Clase. El método get sirve para acceder a la Primary Key de esa clase
    print(result)

    print("\n #2. Obtener todos los objetos de una tabla")
    result = db.session.query(Persona).all() # Solicitamos todos los registros de la clase Persona
    for objeto in result: # Como resultado nos devuelve un objeto, encesitaos hacer un bucle For para ver su contenido
        print("\t- Nombre: {} ---> Edad: {}".format(objeto.nombre, objeto.edad))

    print("\n #3. Obtener el primer objeto de una consulta")
    result = db.session.query(Persona).first() # Devuelve el registro más antiguo de la tabla, es decir, el primero que se registró.
    print(result)

    print("\n #4 Contar. el número de elementos devueltos por una consulta")
    result = db.session.query(Persona).count() # Devuelve cuantos elementos contiene la tabla Persona
    print(result)

    print("\n #5 Ordenar el resultado de una consulta")
    result = db.session.query(Persona).order_by("nombre").all()  # Ordena los datos de una consulta por la columna nombre y los muestra todos
    for objeto in result:
        print("\t- Nombre: {} ---> Edad: {}".format(objeto.nombre, objeto.edad))

    print("\n #6 Ordenar el resultado de una consulta y mostrar los 3 primeros resultados")
    result = db.session.query(Persona).order_by("nombre").limit(3) # Ordena los datos por la columna nombre y muestra los 3 primeros registos
    for objeto in result:
        print("\t- Nombre: {} ---> Edad: {}".format(objeto.nombre, objeto.edad))

    print("\n #7 Aplicar filtros a una consulta con filter")
    result = db.session.query(Persona).filter(Persona.edad < 25).all() # Muestra todos los registros de la clase Persona cuya edad sea menor a 25 años
    for objeto in result:
        print("\t- Nombre: {} ---> Edad: {}".format(objeto.nombre, objeto.edad))

    print("\n #8 Aplicar filtro ilike")
    result = db.session.query(Persona).filter(Persona.nombre.ilike("Sa%")).all() # Muestra todos los resultados de la clase Persona, cuyo nombre empiece por Sa
    for objeto in result:
        print("\t- Nombre: {} ---> Edad: {}".format(objeto.nombre, objeto.edad))

    print("\n #9 Aplicar filtro in_") # Se añade un _ al in porque lin es una palabra reservada de python y no podemos usarla directamente en SQLAlchemy
    #result = db.session.query(Persona).filter(Persona.id_persona.in_([1, 2])).all()  # Devuelve todos los registros que si dentro de la Clase Persona, tenemos los id 1 o 2
    result = db.session.query(Persona).filter(Persona.nombre.in_(["Cristian", "Carlos"])).all()  # Devuelve todos los registros que dentro de la Clase Persona, tengan  los nombres Carlos o Cristian
    for objeto in result:
        print("\t- Nombre: {} ---> Edad: {}".format(objeto.nombre, objeto.edad))

    print("\n #10 Aplicar filtro and_") # La sintaxis funciona como si and_ fuera una función y los parametros sus condicionales
    result = db.session.query(Persona).filter(and_(Persona.id_persona > 2, Persona.nombre.ilike(("D%")))).all() # Devuelve todos los registros que si dentro de la Clase Persona, que su id sea ayor a 2 y su nombre empiece por D
    for objeto in result:
        print("\t- Nombre: {} ---> Edad: {}".format(objeto.nombre, objeto.edad))

    print("\n #11 Aplicar filtro or_") # Los métodos and_ y or_ deben importarse
    result = db.session.query(Persona).filter(or_(Persona.id_persona > 2, Persona.nombre.ilike(("D%")))).all() # Devuelve todos los registros que si dentro de la Clase Persona, que su id sea ayor a 2 o su nombre empiece por D
    for objeto in result:
        print("\t- Nombre: {} ---> Edad: {}".format(objeto.nombre, objeto.edad))

    print("\n #12 Ejecutar instrucciones SQL explicitamente")  # ORM nos permite ejecutar instrucciones SQL. el método text hay que importarlo
    result = db.session.query(Persona).from_statement(text("SELECT * FROM persona")).all() # Dentro del método text() introducimos las instrucciones en lenguaje SQL
    for objeto in result:
        print("\t- Nombre: {} ---> Edad: {}".format(objeto.nombre, objeto.edad))

def aniadirPersona(): # Agrega una persona a la BBDD
    print("\n > Agregar Personas")

    nombre = input("Nombre de la Persona: ")
    edad = input("Edad de la persona: ")
    p = Persona(nombre, edad) # Objeto de la Clase Persona
    db.session.add(p) # Añade la variable p que contiene el objeto Persona a la BD
    db.session.commit()
    db.session.close()
    print("Persona Creada")

def editarPersona():
    print("\n > Editar Personas")

    persona_id = int(input("ID de la persona: "))
    person = db.session.query(Persona).filter(Persona.id_persona == persona_id).first() # Buscamos en la BD por id_persona
    print(person)

    if person is None:
        print("La persona indicada no existe")
    else:
        edad_nueva = int(input("Introduzca la nueva edad: "))
        person.edad = edad_nueva # Modificamos el atributo edad del objeto person
        db.session.commit()
        db.session.close()
        print("Persona ACTUALIZADA")

def borrarPersona():
    print("\n > Borrar Personas")

    persona_id = int(input("ID de la persona: "))
    person = db.session.query(Persona).filter(Persona.id_persona == persona_id).first()  # Buscamos en la BD por id_persona y lo guardamos en una variable
    print(person)

    if person is None:
        print("La persona indicada no existe")
    else:
        db.session.delete(person) # Eliminanos el objeto de la BD
        db.session.commit()
        db.session.close()
        print("Persona BORRADA")

def verPersonas():
    print("\n > Ver Personas")

    personas = db.session.query(Persona).all() # Muestra todos los registros de la Clase Persona
    for p in personas:
        print("\t- ID: {} ---> Nombre: {} ---> Edad: {}".format(p.id_persona, p.nombre, p.edad))



if __name__ == "__main__":
    #db.Base.metadata.drop_all(bind=db.engine, checkfirst=True)  # Elimina la base de datos si esta ya existe

    # En la siguiente linea estamos indicando a SQLArchemy que cree, si no existen, las tablas de todos
    # los modelos que encuentre en models.py. Sin embargo, para que esto ocurra es necesario que cualquier
    # modelo se haya importado previamente antes de llamar a la siguiente función (create_all())
    db.Base.metadata.create_all(db.engine)

    # Creamos un menú para interactuar con la base de datos a través de ORM
    while(True):
        print("\n1. Agregar personas iniciales\n"
                "2. Consultas de prueba\n"
                "3. Añadir una Persona\n"
                "4. Editar una Persona\n"
                "5. Eliminar una Persona\n"
                "6. Ver Personas\n"
                "7. Salir")

        opcion = int(input("Introduzca una opción: "))
        if opcion == 1:
            agregarPersonasIniciales()
        elif opcion == 2:
            consultasDePrueba()
        if opcion == 3:
            aniadirPersona()
        if opcion == 4:
            editarPersona()
        if opcion == 5:
            borrarPersona()
        if opcion == 6:
            verPersonas()
        elif opcion == 7:
            sys.exit(1) # Este método es la forma correcta de salir de un programa. Como argumento podemos pasar varios números en función del objetivo a conseguir
        else:
            print("Opción no válida")