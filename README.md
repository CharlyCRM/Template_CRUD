# Practicar CRUD con SQLAlchemy

Este pequeño programa de consola me sirvió para aprender a trabajar con un ORM: crear personas, consultarlas, cambiar su edad y eliminarlas sin escribir SQL para cada operación.

## Qué contiene

`main.py` reúne un menú y ejemplos de consultas: filtros, ordenación, límites, condiciones AND/OR y una consulta SQL explícita. `models.py` define la entidad `Persona`; `db.py` conecta con `database/personas.db`.

El menú también permite insertar un grupo de personas de ejemplo. Repetir esa opción añade registros; no reinicia la base.

## Revisarlo en local

No hay un archivo de dependencias fijadas. Necesitas Python y SQLAlchemy en un entorno aislado. Usa una copia de la base SQLite y asegúrate de ejecutar desde la raíz del repositorio, porque la ruta es relativa.

`python main.py` inicia el menú, crea las tablas si faltan y puede modificar o borrar registros según la opción elegida. No lo ejecutes sobre datos que quieras conservar.

## Lo que muestra y lo que falta

Es una práctica de consultas y persistencia, no una plantilla de aplicación completa. Las entradas y el control de flujo conservan las decisiones del ejercicio; no hay pruebas automatizadas ni validación exhaustiva.

Mantengo el código como referencia de mis primeros pasos con SQLAlchemy. Esta revisión mejora la explicación, sin convertirlo en un producto terminado.
