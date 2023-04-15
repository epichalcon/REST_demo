from pydantic import BaseModel


class User(BaseModel):
    nick: str
    name: str
    surname: str
