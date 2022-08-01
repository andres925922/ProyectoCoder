class BaseEntityNotFoundError(Exception):
    pass

class MultipleEntitiesFoundedError(Exception):
    pass

class EntityAlreadyCreatedError(Exception):
    pass

class EntityCouldNotBeenCreated(Exception):
    pass