from Base.models import About


class About_DTO():
    def __init__(self, **kargs) -> None:
        self.id = kargs.get("x")["id"]
        self.nombre = kargs.get("x")["nombre"]
        self.apellido = kargs.get("x")["apellido"]
        self.description = kargs.get("x")["description"]
        self.img = kargs.get("x")["img"]

    def __getitem__(self, key):
        try:
            return self.__dict__[key]
        except IndexError:
            return {}

def _dto_constructor_about(person: About, DTO):
    return DTO(x = person)

def get_about():
    return [
        _dto_constructor_about(person, About_DTO) for person in About.objects.all()
        ]

