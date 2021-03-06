from Base.models import About
from Users.models import Avatar


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

    @classmethod
    def _dto_constructor_about(cls, person: About, DTO):
        return DTO(x = person)

def get_about():
    """
    # Función que retorna la data de los creadores de la aplicación
    """
    return [
        About_DTO
        ._dto_constructor_about(person, About_DTO) for person in About.objects.all()
        ]

def get_avatar(user):
    """
    # user: User
    # Función que permite obtener el avatar del usuario
    """
    avatar = Avatar.objects.select_related().filter(user = user)[0].img

    if avatar:
        return avatar
    else:
        return None

def get_information(user):

    if user != 'AnonymousUser':
        return {
            'avatar': get_avatar(user.id),
            'founders': get_about()
        }
    else:
        return {
            'avatar': None,
            'founders': get_about()
        }
