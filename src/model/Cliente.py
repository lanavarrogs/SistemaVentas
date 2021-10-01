from model.Usuario import Usuario

class Cliente(Usuario):

    def __init__(self,id,nombre,email,edad,telefono,direccion) -> None:
        super().__init__(id,nombre,email,edad,telefono,direccion)
        
    def __str__(self) -> str:
        return super().__str__()