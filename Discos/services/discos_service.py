

from Discos.models import (
    Discos, 
    Genero,
    Banda
)

from Base.exceptions import EntityCouldNotBeenCreated, BaseEntityNotFoundError

# -------------------------------------------------------------
# GENERO SERVICE
# -------------------------------------------------------------

class Genero_Service():

    def get_generos(self):
        return Genero.objects.filter(deleted = False)

    # def create_genero(self, data = None):

    #     if data != None:
    #         try:
    #             genero = Genero(data)
    #         except:
    #             raise EntityCouldNotBeenCreated('Se ha producido un error al crear la entidad')

    #         genero.save()
    # Solucionado con el save del form. No hace falta

    def baja_genero(self, data = None) -> None:
        if data != None:
            try:
                genero = Genero.objects.filter(id = data)[0]
            except:
                raise BaseEntityNotFoundError('No se encontró la entidad')

            genero.deleted = True
            genero.save()