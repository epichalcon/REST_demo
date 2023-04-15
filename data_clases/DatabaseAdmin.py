from typing import Dict

from data_clases.DataClasses import User


class DatabaseAdmin:
    # field of a dictionary of users
    user: Dict[str, User]

    def __init__(self):
        self.user = {}

    def add_user(self, user: User):
        if user.nick in self.user:
            raise AttributeError("User already exists")
        self.user[user.nick] = user

    def get_user(self, nick):
        if nick not in self.user:
            raise KeyError("User does not exist")
        return self.user[nick]

    def update_user(self, nick, user):
        if nick not in self.user:
            raise KeyError("User does not exist")
        self.user[nick] = user

    def delete_user(self, nick):
        if nick not in self.user:
            raise KeyError("User does not exist")
        del self.user[nick]

    def get_users(self, nick_filter, offset, limit):
        pass

    def add_user_friend(self, nick, friend_nick):
        pass

    def delete_user_friend(self, nick, friend_nick):
        pass

    def get_user_friends(self, nick, filter_nick, offset, limit):
        pass

    def add_message(self, message):
        pass

    def get_message(self, message_id):
        pass

    def update_message(self, message_id, message):
        pass

    def delete_message(self, message_id):
        pass

    def get_messages(self, message_filter, offset, limit):
        pass

    def get_user_messages(self, nick, message_filter, offset, limit):
        pass

    def get_user_friends_messages(self, nick, date_filter, message_filter, offset, limit):
        pass

    def get_user_info(self, nick):
        pass
