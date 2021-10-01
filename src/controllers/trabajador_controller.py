import sys
sys.path.append("..")
from model.Trabajador import Trabajador
import mysql.connector
import sys


def stablish_connection():
    try:
        my_db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='p@55W0rD',
            database='construccion'
        )
        print("Conexion con la base de datos exitosa")
        return my_db
    except mysql.connector.Error as err:
        print("Error en la conexion en la base de datos " + err)
        sys.exit(1)

def get_trabajadores():
    db = stablish_connection()
    cursor = db.cursor()
    query = 'SELECT * FROM trabajador'
    cursor.execute(query)
    trabajadores = cursor.fetchall()
    list_trabajador = []

    for trabajador in trabajadores:
        id = trabajador[0]
        nombre = trabajador[1]
        email = trabajador[2]
        edad = trabajador[3]
        telefono = trabajador[4]
        direccion = trabajador[5]

        value_trabajor = Trabajador(id,nombre,email,edad,telefono,direccion)
        list_trabajador.append(value_trabajor)
    db.close()
    return list_trabajador

def set_trabajadores(trabajador):
    try:
        id = str(trabajador.get_id())
        nombre = trabajador.get_nombre()
        email = trabajador.get_email()
        edad = trabajador.get_edad()
        telefono = trabajador.get_telefono()
        direccion = trabajador.get_direccion()
        
        db = stablish_connection()
        cursor = db.cursor()
        query = f'INSERT INTO trabajador VALUES(%s,%s,%s,%s,%s,%s)'
        values = (id,nombre,email,edad,telefono,direccion)
        cursor.execute(query,values)
        
        db.commit()
    except Exception as erro:
        print("El usuario no se agrego")

    



def total_trabajadores():
    db = stablish_connection()
    cursor = db.cursor()
    query = 'SELECT COUNT(id_trabajador) as total FROM trabajador'
    cursor.execute(query)
    total = cursor.fetchone()
    return (int(total[0]))