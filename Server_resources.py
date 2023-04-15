from fastapi import FastAPI, HTTPException, Path, Query
from data_clases.DatabaseAdmin import DatabaseAdmin
from data_clases.DataClasses import User, Message

app = FastAPI()
database_admin = DatabaseAdmin()


@app.get("/")
def index():  # This is the root path
    return {"message": "Hello World"}


@app.post("/users")
def create_user(user: User):
    try:
        database_admin.add_user(user)
        return {"message": "User created"}
    except AttributeError as e:
        HTTPException(status_code=400, detail=str(e))


@app.get("/users/{nick}")
def get_user(nick: str):
    try:
        return database_admin.get_user(nick)
    except KeyError as e:
        HTTPException(status_code=404, detail=str(e))


@app.put("/users/{nick}")
def update_user(nick: str, user: User):
    try:
        database_admin.update_user(nick, user)
        return {"message": "User updated"}
    except KeyError as e:
        HTTPException(status_code=404, detail=str(e))


@app.delete("/users/{nick}")
def delete_user(nick: str):
    try:
        database_admin.delete_user(nick)
        return {"message": "User deleted"}
    except KeyError as e:
        HTTPException(status_code=404, detail=str(e))


@app.get("/users")
def get_all_users(nick_filter: str = None, offset: int = 1, limit: int = 10):
    try:
        return database_admin.get_users(nick_filter, offset, limit)
    except KeyError as e:
        HTTPException(status_code=404, detail=str(e))


@app.post("/users/{nick}/friends/{friend_nick}")
def add_user_friends(nick: str, friend_nick: str):
    try:
        database_admin.add_user_friend(nick, friend_nick)
        return {"message": "Friend added"}
    except AttributeError as e:
        HTTPException(status_code=400, detail=str(e))


@app.delete("/users/{nick}/friends/{friend_nick}")
def delete_user_friends(nick: str, friend_nick: str):
    try:
        database_admin.delete_user_friend(nick, friend_nick)
        return {"message": "Friend deleted"}
    except KeyError as e:
        HTTPException(status_code=404, detail=str(e))


@app.get("/users/{nick}/friends")
def get_user_friends(nick: str, filter_nick: str = None, offset: int = 1, limit: int = 10):
    try:
        return database_admin.get_user_friends(nick, filter_nick, offset, limit)
    except KeyError as e:
        HTTPException(status_code=404, detail=str(e))


@app.post("/messages")
def create_message(message: Message):
    try:
        database_admin.add_message(message)
        return {"message": "Message created"}
    except AttributeError as e:
        HTTPException(status_code=400, detail=str(e))


@app.get("/messages/{message_id}")
def get_message(message_id: int):
    try:
        return database_admin.get_message(message_id)
    except KeyError as e:
        HTTPException(status_code=404, detail=str(e))


@app.put("/messages/{message_id}")
def update_message(message_id: int, message: Message):
    try:
        database_admin.update_message(message_id, message)
        return {"message": "Message updated"}
    except KeyError as e:
        HTTPException(status_code=404, detail=str(e))


@app.delete("/messages/{message_id}")
def delete_message(message_id: int):
    try:
        database_admin.delete_message(message_id)
        return {"message": "Message deleted"}
    except KeyError as e:
        HTTPException(status_code=404, detail=str(e))


@app.get("/messages")
def get_all_messages(message_filter: str = None, offset: int = 1, limit: int = 10):
    try:
        return database_admin.get_messages(message_filter, offset, limit)
    except KeyError as e:
        HTTPException(status_code=404, detail=str(e))


@app.get("/users/{nick}/messages")
def get_user_messages(nick: str, message_filter: str = None, offset: int = 1, limit: int = 10):
    try:
        return database_admin.get_user_messages(nick, message_filter, offset, limit)
    except KeyError as e:
        HTTPException(status_code=404, detail=str(e))


@app.get("/users/{nick}/friends/messages/")
def get_user_friends_messages(nick: str, date_filter: str = None, message_filter: str = None, offset: int = 1,
                              limit: int = 10):
    try:
        return database_admin.get_user_friends_messages(nick, date_filter, message_filter, offset, limit)
    except KeyError as e:
        HTTPException(status_code=404, detail=str(e))


@app.get("/users/{nick}/info")
def get_user_info(nick: str):
    try:
        return database_admin.get_user_info(nick)
    except KeyError as e:
        HTTPException(status_code=404, detail=str(e))
