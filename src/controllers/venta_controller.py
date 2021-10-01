import sys
sys.path.append("..")
from model.Venta import Venta
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

def get_ventas():
    db = stablish_connection()
    cursor = db.cursor()
    query = """SELECT DISTINCT ventas.id_venta,ventas.estatus,ventas.total,ventas.sucursal,cliente.nombre,trabajador.nombre,producto.nombre FROM ventas 
    INNER JOIN producto ON ventas.id_producto = producto.id_producto
    INNER JOIN cliente ON ventas.id_cliente = cliente.id_cliente
    INNER JOIN trabajador ON ventas.id_trabajador = trabajador.id_trabajador
    """
    cursor.execute(query)
    ventas = cursor.fetchall()
    list_ventas = []

    for venta in ventas:
        id = venta[0]
        estatus = venta[1]
        total = venta[2]
        sucursal = venta[3]
        nombre_cliente = venta[4]
        nombre_trabajador = venta[5]
        producto = venta[6]

        value_trabajor = Venta(id,estatus,total,sucursal,nombre_cliente,nombre_trabajador,producto)
        list_ventas.append(value_trabajor)
    db.close()
    return list_ventas

def set_ventas(venta):
    try:
        id = str(venta.get_id())
        status = venta.get_status()
        total = venta.get_total()
        sucursal = venta.get_sucursal()
        cliente = venta.get_cliente()
        trabajador = venta.get_trabajador()
        producto = venta.get_producto()
        
        db = stablish_connection()
        cursor = db.cursor()
        query = f'INSERT INTO ventas VALUES(%s,%s,%s,%s,%s,%s,%s)'
        values = (id,status,total,sucursal,cliente,trabajador,producto)
        cursor.execute(query,values)
        
        db.commit()
    except Exception as error:
        print("La venta no se registro no se agrego" + error)


def total_ventas():
    db = stablish_connection()
    cursor = db.cursor()
    query = 'SELECT COUNT(id_venta) as total FROM ventas'
    cursor.execute(query)
    total = cursor.fetchone()
    return (int(total[0]))

def get_precio_producto(producto):
    db = stablish_connection()
    cursor = db.cursor()
    query = 'SELECT precio FROM producto WHERE nombre = %s'
    val = (producto)
    cursor.execute(query,val)
    total = cursor.fetchone()
    return (float(total[0]))