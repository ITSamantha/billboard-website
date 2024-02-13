import json

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    pass


class BaseResponseSchema:
    id: int

    def jsonify(self: BaseModel):
        return self.model_dump(mode="json")
