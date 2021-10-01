class Producto:

    def __init__(self,id,nombre,precio) -> None:
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio


    def get_id(self) :
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__precio

    def __str__(self) -> str:
        return f'id: {self.__id}, nombre: {self.__nombre} precio: {self.__precio}'