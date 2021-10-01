import sys
sys.path.append("..")
from model.Producto import Producto
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

def get_productos():
    db = stablish_connection()
    cursor = db.cursor()
    query = 'SELECT * FROM producto'
    cursor.execute(query)
    productos = cursor.fetchall()
    list_productos = []
    for producto in productos:
        id = producto[0]
        nombre = producto[1]
        total = producto[2]
        value_producto = Producto(id,nombre,total)
        list_productos.append(value_producto)
    db.close()
    return list_productos

def set_productos(trabajador):
    try:
        id = str(trabajador.get_id())
        nombre = trabajador.get_nombre()
        precio = trabajador.get_email()
    
        db = stablish_connection()
        cursor = db.cursor()
        query = f'INSERT INTO producto VALUES(%s,%s,%s)'
        values = (id,nombre,precio)
        cursor.execute(query,values)
        
        db.commit()
    except Exception as erro:
        print("El usuario no se agrego")

    
def total_productos():
    db = stablish_connection()
    cursor = db.cursor()
    query = 'SELECT COUNT(id_producto) as total FROM producto'
    cursor.execute(query)
    total = cursor.fetchone()
    return (int(total[0]))

