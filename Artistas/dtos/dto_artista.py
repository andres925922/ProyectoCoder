
class DTO_Artista():

    def __init__(self, 
    **kargs) -> None:

        self.id = kargs.get('x').id
        self.nombre = kargs.get('x')['nombre']
        self.apellido = kargs.get('x')['apellido']
        self.nombre_artistico = kargs.get('x')['nombre_artistico']
        self.banda = kargs.get('x')['banda']
        self.historia = kargs.get('x')['historia']


class DTO_Artista_Extended(DTO_Artista):
    
    def __init__(self, discos, **kargs) -> None:
        super().__init__(id, **kargs)
        self.discos = discos
    