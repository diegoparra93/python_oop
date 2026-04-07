from model import User

class UserCollection:
    def __init__(self):
        self._items = []

    def add(self, user):
        if not isinstance(user, User):
            raise TypeError("Solo se permiten objetos User")
        self._items.append(user)

    def remove(self, user):
        self._items.remove(user)

    def get_all(self):
        return self._items