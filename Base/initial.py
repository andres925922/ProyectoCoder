from Artistas.models import Banda, Artista
from Discos.models import Genero, Discos
import datetime

def crear_bandas():
    u2 = Banda(
        nombre = 'U2'
    )

    coldplay = Banda(
        nombre = 'Coldplay'
    )

    marron5 = Banda(
        nombre = 'Marron 5'
    )

    try:
        u2.save()
        coldplay.save()
        marron5.save()
    except:
        raise BaseException('Error al crear las bandas')

def crear_artistas_coldplay():
    coldplay = Banda.objects.get(nombre = 'coldplay')
    chris = Artista(
        nombre = 'Chris',
        apellido = 'Martin',
        nombre_artistico = 'Chris Martin',
        banda = coldplay,
        historia = "Pruebas"
    )

    phill = Artista(
        nombre = 'Phill',
        apellido = 'Harvey',
        nombre_artistico = 'Phill Harvey',
        banda = coldplay,
        historia = "Pruebas"
    )

    will = Artista(
        nombre = 'Will',
        apellido = 'Champion',
        nombre_artistico = 'Will Champion',
        banda = coldplay,
        historia = "Pruebas"
    )
    try:
        phill.save()
        chris.save()
        will.save()
    except:
        raise BaseException('Error al crear los artistas')

def crear_generos():
    rock = Genero(
        nombre = 'rock'
    )
    alternativo = Genero(
        nombre = 'alternativo'
    )
    pop = Genero(
        nombre = 'pop'
    )
    reggae = Genero(
        nombre = 'reggae'
    )
    try:
        rock.save()
        alternativo.save()
        pop.save()
        reggae.save()
    except:
        raise BaseException('Error al cargar los generos')

def crear_discos_coldplay():
    liveInBsAs = Discos(
        nombre = 'live in Buenos Aires',
        year = 2018,
        duration = datetime.timedelta(minutes = 50),
        banda = Banda.objects.get(nombre = 'Coldplay')
    )

    vivaLaVida = Discos(
        nombre = 'Viva la Vida',
        year = 2008,
        duration = datetime.timedelta(minutes = 50),
        banda = Banda.objects.get(nombre = 'Coldplay')
    )

    parachutes = Discos(
        nombre = 'Parachutes',
        year = 2018,
        duration = datetime.timedelta(minutes = 50),
        banda = Banda.objects.get(nombre = 'Coldplay')
    )
    
    try:
        vivaLaVida.save()
        liveInBsAs.save()
        parachutes.save()
    except:
        raise BaseException('Error al crear los discos')

# crear_bandas()
# crear_generos()
# crear_artistas_coldplay()
# crear_discos_coldplay()


