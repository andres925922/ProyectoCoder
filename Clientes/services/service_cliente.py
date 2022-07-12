from ..models import Cliente
from ..dtos.dto_cliente import DTO_Cliente, DTO_Clientes
from typing import List
from ..exceptions import BaseEntityNotFoundError

class Servicio_Cliente:

    def get_all_clientes(self) -> List[DTO_Clientes]:
        """ Taer todos los clientes de la base de datos """
        return [self._dto_constructor(cliente, DTO_Clientes) for cliente in Cliente.objects.all().values()]

    def get_all_clientes_por_estado(self, estado) -> List[DTO_Clientes]:
        """ Taer todos los clientes de la base de datos """
        return [self._dto_constructor(cliente, DTO_Clientes) for cliente in Cliente.objects.filter(estado = estado).values()]

    def get_cliente_por_dni(self, value: str) -> DTO_Cliente:
        """ Value debe ser el número de cliente o el número de dni o identidad """
        try:
            return self._dto_constructor(cliente = Cliente.objects.filter(identity = value).values()[0], DTO=DTO_Cliente)
        except:
            raise BaseEntityNotFoundError("Cliente no encontrado")

    def get_cliente_por_numero_cliente(self, value: str) -> DTO_Cliente:
        """ Value debe ser el número de cliente o el número de dni o identidad """
        try:
            return self._dto_constructor(cliente=Cliente.objects.filter(id_number = value).values()[0], DTO=DTO_Cliente)
        except:
            raise BaseEntityNotFoundError("Cliente no encontrado")
    
    def _dto_constructor(self, cliente: Cliente, DTO):
        return DTO(x = cliente)

