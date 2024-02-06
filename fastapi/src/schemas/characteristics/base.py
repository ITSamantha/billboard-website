from pydantic import BaseModel


class BaseCharacteristic(BaseModel):
    id: int
    title: str

    def __str__(self):
        return self.title
