from src.schemas.base import BaseResponseSchema
from src.schemas.characteristics.base import BaseCharacteristic


# ad priority
class Priority(BaseCharacteristic):
    priority: int


class PriorityResponse(Priority, BaseResponseSchema):
    pass


class PriorityCreate(Priority):
    pass


class PriorityUpdate(Priority):
    pass
