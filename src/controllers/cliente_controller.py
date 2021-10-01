import sys
sys.path.append("..")
from model.Cliente import Cliente
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
        return my_db
    except mysql.connector.Error as err:
        print("Error en la conexion en la base de datos " + err)
        sys.exit(1)



def get_clientes():
    db = stablish_connection()
    cursor = db.cursor()
    query = 'SELECT * FROM cliente'
    cursor.execute(query)
    clientes = cursor.fetchall()
    list_cliente = []

    for cliente in clientes:
        print(cliente)
        id = cliente[0]
        nombre = cliente[1]
        email = cliente[2]
        edad = cliente[3]
        telefono = cliente[4]
        direccion = cliente[5]
        value_cliente= Cliente(id,nombre,email,edad,telefono,direccion)
        list_cliente.append(value_cliente)
    db.close()
    return list_cliente

def set_clientes(cliente):
    try:
        id = str(cliente.get_id())
        nombre = cliente.get_nombre()
        email = cliente.get_email()
        edad = cliente.get_edad()
        telefono = cliente.get_telefono()
        direccion = cliente.get_direccion()
        
        db = stablish_connection()
        cursor = db.cursor()
        query = f'INSERT INTO cliente VALUES(%s,%s,%s,%s,%s,%s)'
        values = (id,nombre,email,edad,telefono,direccion)
        cursor.execute(query,values)
        
        db.commit()
    except Exception as erro:
        print("El usuario no se agrego")

    



def total_clients():
    db = stablish_connection()
    cursor = db.cursor()
    query = 'SELECT COUNT(id_cliente) as total FROM cliente'
    cursor.execute(query)
    total = cursor.fetchone()
    return (int(total[0]))