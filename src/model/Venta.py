class Venta:

    def __init__(self,id,estatus,total,sucursal,cliente,trabajador,producto) -> None:
        self.__id= id
        self.__estatus = estatus
        self.__total = total
        self.__sucursal = sucursal
        self.__cliente = cliente
        self.__trabajador = trabajador
        self.__producto = producto

    def get_id(self):
        return self.__id

    def get_status(self):
        return self.__estatus

    def get_total(self):
        return self.__total

    def get_sucursal(self):
        return self.__sucursal

    def get_cliente(self):
        return self.__cliente
    
    def get_trabajador(self):
        return self.__trabajador

    def get_producto(self):
        return self.__producto

    def __str__(self) -> str:
        return f'id: {self.__id}  estatus:  {self.__estatus}  total: {self.__total}  sucursal: {self.__id}  cliente: {self.__cliente} trabajador: {self.__trabajador} prodcuto: {self.__producto}'