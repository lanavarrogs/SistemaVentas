class Usuario:
    def __init__(self,id,nombre,email,edad,telefono,direccion) -> None:
        self.__id = id
        self.__nombre = nombre
        self.__email = email
        self.__edad = edad
        self.__telefono = telefono
        self.__direccion=direccion

    def get_id(self) :
        return self.__id

    def get_nombre(self):
        return self.__nombre

    def get_email(self):
        return self.__email

    def get_edad(self):
        return self.__edad

    def get_telefono(self):
        return self.__telefono

    def get_direccion(self):
        return self.__direccion
        
    @classmethod
    def comprar_producto():
        pass

    def __str__(self) -> str:
        return f'id: {self.__id}  nombre: {self.__nombre}  email: {self.__email} edad: {self.__edad}  telefono: {self.__telefono} direccion: {self.__direccion}'