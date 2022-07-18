from Base.exceptions import EntityAlreadyCreatedError, MultipleEntitiesFoundedError
from ..models import Cliente
from ..dtos.dto_cliente import DTO_Cliente, DTO_Clientes
from typing import List
from ..exceptions import BaseEntityNotFoundError

class Servicio_Cliente:

    def get_all_clientes_dispite_state(self) -> List[DTO_Clientes]:
        """ Taer todos los clientes de la base de datos """
        return [self._dto_constructor(cliente, DTO_Clientes) for cliente in Cliente.objects.all().values()]

    def get_all_clientes(self, deleted: bool = False) -> List[DTO_Clientes]:
        """ Taer todos los clientes de la base de datos """
        return [self._dto_constructor(cliente, DTO_Clientes) for cliente in Cliente.objects.filter(deleted=deleted).values()]

    def get_all_clientes_por_estado(self, estado: int) -> List[DTO_Clientes]:
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

    def get_cliente_por_id(self, value: str) -> DTO_Cliente:
        """ Value debe ser el número de cliente o el número de dni o identidad """
        try:
            return self._dto_constructor(cliente=Cliente.objects.get(id=value), DTO=DTO_Cliente)
        except:
            raise BaseEntityNotFoundError("Cliente no encontrado")

    def exist_cliente_by_dni_or_id_number( self,
        dni: str = None):
        try: 
            if dni:
                return True if Cliente.objects.get(identity = dni) else False
        except:
            return False


    def crear_cliente(
        self,
        cliente: Cliente
    ) -> DTO_Cliente:
        try:
            # Evaluamos si el cliente existe sino retornamos una excepción
            cliente_por_dni = self.get_cliente_por_dni(value=cliente.identity)
            cliente_por_numero_cliente = self.get_cliente_por_numero_cliente(value=cliente.id_number)
            if cliente_por_dni or cliente_por_numero_cliente:
                raise EntityAlreadyCreatedError("El dni del cliente o su número de cliente ya se encuentran registrados")
        except:
            cliente.save()
            return self._dto_constructor(cliente=cliente, DTO=DTO_Cliente)   

    def actualizar_cliente(
        self,
        cliente: Cliente,
    ) -> DTO_Cliente:
        if cliente.id_number:
            u_cliente = Cliente.objects.get(id_number=cliente.id_number)
            # EVALUATE UNIQUE CONSTRAINT
            if(
                u_cliente.identity != cliente.identity
            ):
            # Si el dni o el numero de cliente es diferente al que pasamos evaluamos si tanto el dni o el numero existen
                exists: bool = self.exist_cliente_by_dni_or_id_number(
                    dni= cliente.identity if u_cliente.identity != cliente.identity else None,
                )
                if exists:
                    raise EntityAlreadyCreatedError("Valores ya existentes")
            u_cliente.id_number = cliente.id_number
            u_cliente.nombre = cliente.nombre
            u_cliente.apellido = cliente.apellido
            u_cliente.identity = cliente.identity
            u_cliente.email = cliente.email
            u_cliente.sexo = cliente.sexo
            u_cliente.tel = cliente.tel
            u_cliente.estado = cliente.estado
            u_cliente.save()
            return self._dto_constructor(cliente=cliente, DTO=DTO_Cliente)

        else:
            raise Exception("No se han provisto datos suficientes para actualizar el cliente")
             

    def eliminar_cliente(self, id_cliente: int = None):
        if id_cliente:
            try: 
                cliente = Cliente.objects.get(id_number = id_cliente)
                cliente.deleted = True
                cliente.save()
                return self._dto_constructor(cliente=cliente, DTO=DTO_Cliente)
            except:
                raise BaseEntityNotFoundError("Id de cliente no encontrada en la bd")
        
        raise Exception("No se han provisto datos suficientes para eliminar el cliente")
            

    def _dto_constructor(self, cliente: Cliente, DTO):
        return DTO(x = cliente)

