class DTO_Cliente:
    def __init__(self, **kargs) -> None:
        self.id = kargs.get("x")["id"]
        self.numero_cliente = kargs.get("x")["id_number"]
        self.nombre = kargs.get("x")["nombre"]
        self.apellido = kargs.get("x")["apellido"]
        self.email = kargs.get("x")["email"]
        self.sexo = kargs.get("x")["sexo"]
        self.tel = kargs.get("x")["tel"]
        self.dni = kargs.get("x")["identity"]
        self.estado = kargs.get("x")["estado"]
    
    def __getitem__(self, key):
        return self.__dict__[key]

class DTO_Clientes:
    def __init__(self, **kargs) -> None:
        self.numero_cliente = kargs.get("x")["id_number"]
        self.nombre = kargs.get("x")["nombre"]
        self.apellido = kargs.get("x")["apellido"]
        self.dni = kargs.get("x")["identity"]
        self.estado = kargs.get("x")["estado"]

    def __getitem__(self, key):
        try:
            return self.__dict__[key]
        except IndexError:
            return {}