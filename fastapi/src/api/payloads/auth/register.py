from pydantic import BaseModel


class RegisterPayload(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: str
    user_status_id: int
    # avatar_id: int
