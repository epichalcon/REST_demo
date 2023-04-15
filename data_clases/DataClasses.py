from pydantic import BaseModel


class User(BaseModel):
    nick: str
    name: str
    surname: str


class Message(BaseModel):
    message_id: int
    nick: str
    message: str
    date: str
